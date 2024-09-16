<script setup lang="ts">
import { onMounted, ref, watch } from 'vue'

// @ts-ignore
import * as d3 from 'd3'

import useProjectStore from '@/stores/ProjectStore'
import useAnalyzeStore from '@/stores/AnalyzeStore'

const colors_item: { [key: number]: string } = {
  1: 'rgba(176, 224, 230, 0.8)',
  2: 'rgba(132, 198, 155, 0.8)',
  3: 'rgba(233, 69, 96, 0.8)',
  4: 'rgba(222, 206, 156, 0.8)',
  5: 'rgba(169, 169, 169, 0.8)'
}

const store_project = useProjectStore()
const store_analyze = useAnalyzeStore()

const date_select = ref('')

onMounted(async () => {
  await store_project.fetchItemRange()

  store_project.items_range.forEach((d: any) => {
    d.datetime_start = new Date(d.datetime_start)
    d.datetime_end = new Date(d.datetime_end)
  })

  createGanttChart()
})

watch(
  () => date_select.value,
  (value_new) => {
    store_analyze.setDate(value_new)
  }
)

function createGanttChart() {
  const margin = { top: 40, right: 0, bottom: 40, left: 50 }
  const height_bar = 5
  const width_bat_min = 13
  const width = 1500 - margin.left - margin.right
  const height = store_project.items_range.length * (height_bar + 2)

  const svg = d3
    .select('#ganttChart')
    .append('svg')
    .attr('width', width + margin.left + margin.right)
    .attr('height', height + margin.top + margin.bottom)
    .append('g')
    .attr('transform', `translate(${margin.left},${margin.top})`)

  const x = d3
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

  const currentDate = new Date()
  const currentX = x(currentDate)

  svg
    .append('line')
    .attr('x1', currentX)
    .attr('y1', -3)
    .attr('x2', currentX)
    .attr('y2', height + 7)
    .attr('stroke', 'red')
    .attr('stroke-width', 1.5)
    .style('opacity', 0.7)

  const verticalLine = svg
    .append('line')
    .attr('stroke', '#909090')
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
      const calculatedWidth = x(d.datetime_end) - x(d.datetime_start)
      return calculatedWidth === 0 ? x(d.datetime_start) - width_bat_min : x(d.datetime_start)
    })
    .attr('y', (d: any) => y(d.rid + ':' + d.title))
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

  const dateBackground = svg
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
      const [mouseX, mouseY] = d3.pointer(event)
      const hoveredDate = x.invert(mouseX).toISOString().split('T')[0]

      verticalLine
        .attr('x1', mouseX)
        .attr('y1', -3)
        .attr('x2', mouseX)
        .attr('y2', height + 7)
        .attr('stroke-width', 1.5)
        .style('opacity', 0.8)

      const textWidth = hoveredDate.length * 7
      dateBackground
        .attr('x', mouseX + 10)
        .attr('y', mouseY)
        .attr('width', textWidth + 20)
        .attr('height', 20)
        .style('opacity', 0.9)

      dateText
        .attr('x', mouseX + 20)
        .attr('y', mouseY + 15)
        .text(hoveredDate)
        .style('opacity', 0.9)
    })
    .on('mouseout', () => {
      verticalLine.style('opacity', 0)
      dateText.style('opacity', 0)
      dateBackground.style('opacity', 0)
    })
    .on('click', function (event: any) {
      const [mouseX] = d3.pointer(event)
      date_select.value = x.invert(mouseX).toISOString().split('T')[0]
    })
}
</script>

<template>
  <div id="ganttChart"></div>
</template>

<style scoped>
svg {
  font-family: sans-serif;
}
</style>
