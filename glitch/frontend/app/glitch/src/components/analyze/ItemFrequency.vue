<script setup lang="ts">
import { onMounted } from 'vue'

// @ts-ignore
import * as d3 from 'd3'

import type { ItemFrequency } from '@/types/Item'
import useSummaryStore from '@/stores/SummaryStore'
import useAnalyzeStore from '@/stores/AnalyzeStore'

const props = defineProps<{
  id_project: number | null
}>()

const store_analyze = useAnalyzeStore()
const store_summary = useSummaryStore()

let svg: any
let format_time: any

onMounted(async () => {
  await store_analyze.fetchItemsFrequency(props.id_project)
  await store_summary.fetchSummaryProject(props.id_project)

  createCalendar()
})

function createCalendar() {
  const size_cell = 20
  const radius = 4
  const width = 53 * size_cell
  const height = 7 * size_cell

  svg = d3
    .select('#calendar')
    .append('svg')
    .attr('width', width)
    .attr('height', height + 20)
    .append('g')
    .attr('transform', `translate(20,20)`)

  format_time = d3.timeFormat('%Y-%m-%d')

  const date_end = new Date(2024, 8, 30)
  const date_start = new Date(date_end.getFullYear() - 1, date_end.getMonth(), 1)
  const days = d3.timeDays(date_start, date_end)

  const colors_task = ['rgba(0, 0, 255, 0.2)', 'rgba(0, 0, 255, 0.8)']
  const colors_bug = ['rgba(255, 0, 0, 0.2)', 'rgba(255, 0, 0, 0.8)']

  const max_task = d3.max(store_analyze.items_frequency, (d: ItemFrequency) => d.task_count)
  const max_bug = d3.max(store_analyze.items_frequency, (d: ItemFrequency) => d.bug_count)

  const color_scale_task = d3
    .scaleQuantize()
    .domain([0, max_task || 1])
    .range(colors_task)
  const color_scale_bug = d3
    .scaleQuantize()
    .domain([0, max_bug || 1])
    .range(colors_bug)

  const tooltip = d3
    .select('#calendar')
    .append('div')
    .attr('class', 'tooltip')
    .style('opacity', 0)
    .style('position', 'absolute')
    .style('background', 'rgba(0, 0, 0, 0.7)')
    .style('color', '#fff')
    .style('margin', '10px')
    .style('padding', '5px')
    .style('border-radius', '5px')
    .style('pointer-events', 'none')

  svg
    .selectAll('rect')
    .data(days)
    .enter()
    .append('rect')
    .attr('width', size_cell)
    .attr('height', size_cell)
    .attr('x', (d: any) => {
      const date_start = new Date(2023, 9, 1)
      const count_week = d3.timeWeek.count(date_start, d)
      return count_week * size_cell
    })
    .attr('y', (d: any) => d.getDay() * size_cell)
    .attr('rx', radius)
    .attr('ry', radius)
    .attr('fill', (d: any) => {
      const date = format_time(d)
      const data = store_analyze.items_frequency.find((item) => {
        const date_item = item.datetime_entry.split(' ')[0]
        return date_item === date
      })

      if (data) {
        if (data.task_count > 0 && data.bug_count > 0) {
          const color_task = d3.color(color_scale_task(data.task_count))!.rgb()
          const color_bug = d3.color(color_scale_bug(data.bug_count))!.rgb()
          const color_blended = d3.rgb(
            color_task.r * 0.4 + color_bug.r * 0.6,
            color_task.g * 0.4 + color_bug.g * 0.6,
            color_task.b * 0.4 + color_bug.b * 0.6
          )
          return color_blended.toString()
        } else if (data.bug_count > 0) {
          return color_scale_bug(data.bug_count)
        } else if (data.task_count > 0) {
          return color_scale_task(data.task_count)
        }
      }
      return '#0f0f0f'
    })
    .attr('stroke', '#000000')
    .attr('stroke-width', 1.5)
    .style('opacity', 0.8)
    .attr('data-date', (d: any) => format_time(d))
    .on('mouseover', function (event: any, d: any) {
      const date = format_time(d)
      const data = store_analyze.items_frequency.find((item) => {
        const date_item = item.datetime_entry.split(' ')[0]
        return date_item === date
      })

      let tooltipContent = `<strong>${date}</strong><br/>`
      if (data) {
        tooltipContent += `Task:${data.task_count}, Bug:${data.bug_count}`
      } else {
        tooltipContent += `no data.`
      }

      tooltip
        .html(tooltipContent)
        .style('left', event.pageX + 10 + 'px')
        .style('top', event.pageY - 28 + 'px')
        .transition()
        .duration(200)
        .style('opacity', 0.8)
    })
    .on('mousemove', function (event: any) {
      tooltip.style('left', event.pageX + 10 + 'px').style('top', event.pageY - 28 + 'px')
    })
    .on('mouseout', function () {
      tooltip.transition().duration(500).style('opacity', 0)
    })
}
</script>

<template>
  <div id="calendar"></div>
</template>

<style scoped>
#calendar {
  margin: 0 0 30px 70px;
}

svg {
  font-family: sans-serif;
}
</style>
