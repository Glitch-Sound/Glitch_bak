<script setup lang="ts">
import { onMounted } from 'vue'

// @ts-ignore
import * as d3 from 'd3'

import useProjectStore from '@/stores/ProjectStore'

const store_project = useProjectStore()

const taskColors: { [key: number]: string } = {
  1: 'rgba(176, 224, 230, 0.8)',
  2: 'rgba(132, 198, 155, 0.8)',
  3: 'rgba(233, 69, 96, 0.8)',
  4: 'rgba(222, 206, 156, 0.8)',
  5: 'rgba(169, 169, 169, 0.8)'
}

onMounted(async () => {
  await store_project.fetchProjectSummary()

  store_project.summary_project.forEach((d: any) => {
    d.datetime_start = new Date(d.datetime_start)
    d.datetime_end = new Date(d.datetime_end)
  })

  createGanttChart()
})

function createGanttChart() {
  const margin = { top: 20, right: 30, bottom: 40, left: 100 }
  const taskBarHeight = 10
  const minTaskBarWidth = 20
  const width = 1500 - margin.left - margin.right
  const height = store_project.summary_project.length * (taskBarHeight + 5)

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
      d3.min(store_project.summary_project, (d: any) => d.datetime_start),
      d3.max(store_project.summary_project, (d: any) => d.datetime_end)
    ])
    .range([0, width])

  const y = d3
    .scaleBand()
    .domain(store_project.summary_project.map((d) => d.rid + ':' + d.title))
    .range([0, height])
    .padding(0.3)

  // svg.append('g').call(d3.axisLeft(y))

  svg
    .append('text')
    .attr('text-anchor', 'middle')
    .attr('transform', `translate(-60,${height / 2})rotate(-90)`)
    .attr('fill', 'black')
    .attr('font-size', '50px')
    .text('Task Titles')

  svg
    .selectAll('rect')
    .data(store_project.summary_project)
    .enter()
    .append('rect')
    .attr('x', (d: any) => {
      const calculatedWidth = x(d.datetime_end) - x(d.datetime_start)
      return calculatedWidth === 0 ? x(d.datetime_start) - minTaskBarWidth : x(d.datetime_start)
    })
    .attr('y', (d: any) => y(d.rid + ':' + d.title))
    .attr('width', (d: any) => {
      const calculatedWidth = x(d.datetime_end) - x(d.datetime_start)
      return calculatedWidth === 0 ? minTaskBarWidth : Math.max(calculatedWidth, minTaskBarWidth)
    })
    .attr('height', taskBarHeight)
    .attr('rx', 5)
    .attr('ry', 5)
    .attr('fill', (d: any) => taskColors[d.state])
    .attr('stroke', 'black')
    .attr('stroke-width', 1)
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
