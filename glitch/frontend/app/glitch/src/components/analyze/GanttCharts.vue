<script setup lang="ts">
import { onMounted, ref, watch } from 'vue'

// @ts-ignore
import * as d3 from 'd3'

import useProjectStore from '@/stores/ProjectStore'
import useAnalyzeStore from '@/stores/AnalyzeStore'

const colors_item: { [key: number]: string } = {
  1: 'rgba(176, 224, 230, 0.7)',
  2: 'rgba(132, 198, 155, 0.7)',
  3: 'rgba(233, 69, 96, 0.7)',
  4: 'rgba(222, 206, 156, 0.7)',
  5: 'rgba(169, 169, 169, 0.7)'
}

const store_project = useProjectStore()
const store_analyze = useAnalyzeStore()

const date_selected = ref('')
const date_hovered = ref('')

onMounted(async () => {
  store_project.fetchItemRange()
})

watch(
  () => store_project.items_range,
  () => {
    store_project.items_range.forEach((d: any) => {
      d.datetime_start = new Date(d.datetime_start)
      d.datetime_end = new Date(d.datetime_end)
    })
    createGanttChart()
  }
)

watch(
  () => date_selected.value,
  (value_new) => {
    store_analyze.setDateSelected(value_new)
  }
)

function createGanttChart() {
  const margin = { top: 20, right: 100, bottom: 40, left: 50 }
  const height_bar = 5
  const width_bat_min = 13
  const width = 1600 - margin.left - margin.right
  const height = store_project.items_range.length * (height_bar + 2)

  d3.select('#gantt-chart').selectAll('svg').remove()

  const svg = d3
    .select('#gantt-chart')
    .append('svg')
    .attr('width', width + margin.left + margin.right)
    .attr('height', height + margin.top + margin.bottom)
    .append('g')
    .attr('transform', `translate(${margin.left},${margin.top})`)

  let line_date_selected: any
  let x: any

  x = d3
    .scaleTime()
    .domain([
      d3.min(store_project.items_range, (d: any) => d.datetime_start),
      d3.max(store_project.items_range, (d: any) => d.datetime_end)
    ])
    .range([0, width])

  const y = d3
    .scaleBand()
    .domain(store_project.items_range.map((d) => d.rid + ':' + d.title))
    .range([0, height])
    .padding(0.5)

  const x_current = x(new Date())

  svg
    .append('line')
    .attr('x1', x_current)
    .attr('y1', -3)
    .attr('x2', x_current)
    .attr('y2', height + 7)
    .attr('stroke', '#cdcd00')
    .attr('stroke-width', 1.0)
    .style('opacity', 0.7)

  line_date_selected = svg
    .append('line')
    .attr('x1', x_current)
    .attr('y1', -3)
    .attr('x2', x_current)
    .attr('y2', height + 7)
    .attr('stroke', '#cdcd00')
    .attr('stroke-width', 2.2)
    .style('opacity', 0.7)

  const line_vertical = svg
    .append('line')
    .attr('stroke', '#9f9f9f')
    .attr('stroke-width', 1.5)
    .attr('y1', -3)
    .attr('y2', height + 7)
    .attr('stroke-width', 1.5)
    .style('opacity', 0)

  svg
    .selectAll('rect')
    .data(store_project.items_range)
    .enter()
    .append('rect')
    .attr('x', (d: any) => {
      const width_calculated = x(d.datetime_end) - x(d.datetime_start)
      return width_calculated === 0 ? x(d.datetime_start) - width_bat_min : x(d.datetime_start)
    })
    .attr('y', (d: any) => {
      const yValue = y(d.rid + ':' + d.title)
      return yValue !== undefined ? yValue : 0
    })
    .attr('width', (d: any) => {
      const width = x(d.datetime_end) - x(d.datetime_start)
      return width === 0 ? width_bat_min : Math.max(width, width_bat_min)
    })
    .attr('height', height_bar)
    .attr('rx', 3)
    .attr('ry', 3)
    .attr('fill', (d: any) => colors_item[d.state])
    .attr('stroke', 'black')
    .attr('stroke-width', 1)

  const background_date = svg
    .append('rect')
    .attr('fill', 'rgba(0, 0, 0, 0.9)')
    .attr('rx', 5)
    .attr('ry', 5)
    .style('opacity', 0)

  const dateText = svg
    .append('text')
    .attr('fill', '#f0f0f0')
    .attr('font-size', '14px')
    .attr('text-anchor', 'start')
    .style('opacity', 0)

  svg
    .append('rect')
    .attr('width', width)
    .attr('height', height)
    .attr('fill', 'none')
    .attr('pointer-events', 'all')
    .on('mousemove', function (event: any) {
      const [mouse_x, mouse_y] = d3.pointer(event)
      date_hovered.value = x.invert(mouse_x).toISOString().split('T')[0]

      line_vertical
        .attr('x1', mouse_x)
        .attr('y1', -3)
        .attr('x2', mouse_x)
        .attr('y2', height + 7)
        .attr('stroke-width', 1.5)
        .style('opacity', 0.8)

      const width_text = date_hovered.value.length * 7
      background_date
        .attr('x', mouse_x + 10)
        .attr('y', mouse_y)
        .attr('width', width_text + 20)
        .attr('height', 20)
        .style('opacity', 0.9)

      dateText
        .attr('x', mouse_x + 20)
        .attr('y', mouse_y + 15)
        .text(date_hovered.value)
        .style('opacity', 0.9)
    })
    .on('mouseout', () => {
      line_vertical.style('opacity', 0)
      dateText.style('opacity', 0)
      background_date.style('opacity', 0)
    })
    .on('click', function (event: any) {
      const [mouse_x] = d3.pointer(event)
      date_selected.value = x.invert(mouse_x).toISOString().split('T')[0]
      line_date_selected.attr('x1', mouse_x).attr('x2', mouse_x).style('opacity', 0.7)
    })
    .on('dblclick', function () {
      date_selected.value = ''
      line_date_selected.attr('x1', x_current).attr('x2', x_current).style('opacity', 0.7)
    })
}
</script>

<template>
  <div id="gantt-chart"></div>
</template>

<style scoped>
svg {
  font-family: sans-serif;
}
</style>
