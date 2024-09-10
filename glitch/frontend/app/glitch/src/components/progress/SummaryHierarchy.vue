<script setup lang="ts">
import { onMounted, watch } from 'vue'

// @ts-ignore
import * as d3 from 'd3'

import useItemStore from '@/stores/ItemStore'
import useProgressStore from '@/stores/ProgressStore'

const props = defineProps<{
  id_project: number | null
  rid_users: number | null
}>()

const store_item = useItemStore()
const store_progress = useProgressStore()

onMounted(async () => {
  await store_item.fetchHierarchy(props.id_project)
  createSunburstChart(props.rid_users)
})

watch(
  () => store_progress.rid_users,
  (value_new) => {
    d3.select(`#sunburst`).selectAll('svg').remove()
    createSunburstChart(value_new)
  }
)

function createSunburstChart(rid_users: number | null) {
  const width = 350
  const radius = 160

  const partition = d3.partition().size([2 * Math.PI, radius])

  const root = d3
    .hierarchy(store_item.hierarchy)
    .sum((d: any) => d.workload_task + d.workload_bug)
    .sort((a: any, b: any) => b.value - a.value)

  partition(root)

  const svg = d3
    .select('#sunburst')
    .append('svg')
    .attr('width', width)
    .attr('height', width)
    .append('g')
    .attr('transform', `translate(${width / 2},${width / 2})`)

  const arc = d3
    .arc()
    .startAngle((d: any) => d.x0)
    .endAngle((d: any) => d.x1)
    .innerRadius((d: any) => d.y0)
    .outerRadius((d: any) => d.y1)

  const color = d3
    .scaleOrdinal()
    .domain(root.descendants().map((d: any) => d.depth))
    .range(d3.schemeCategory10)

  const max_depth = Math.max(...root.descendants().map((d: any) => d.depth))

  const path = svg
    .selectAll('path')
    .data(root.descendants())
    .enter()
    .append('path')
    .attr('d', arc as any)
    .style('fill', (d: any) => {
      if (d.depth === 0) {
        return 'black'
      } else if (d.depth === max_depth) {
        return color(d.depth)
      }
      return color(d.depth)
    })
    .style('stroke', '#000000')
    .style('fill-opacity', (d: any) => {
      if (d.depth === max_depth) {
        return d.data.rid_users === rid_users ? 1 : 0.1
      }
      return 1
    })

  const label = svg
    .append('text')
    .attr('text-anchor', 'middle')
    .attr('fill', '#cdcdcd')
    .style('visibility', 'hidden')

  label
    .append('tspan')
    .attr('class', 'percentage')
    .attr('x', 0)
    .attr('y', 0)
    .attr('dy', '0.35em')
    .attr('font-size', '2em')
    .text('')

  svg
    .append('g')
    .attr('fill', 'none')
    .attr('pointer-events', 'all')
    .on('mouseleave', () => {
      path.attr('fill-opacity', 1)
      label.style('visibility', 'hidden')
    })
    .selectAll('path')
    .data(
      root.descendants().filter((d: any) => {
        return d.depth
      })
    )
    .join('path')
    .attr('d', arc)
    .on('mouseenter', (event: any, d: any) => {
      const sequence = d.ancestors().reverse().slice(1)
      path.attr('fill-opacity', (node: any) => (sequence.indexOf(node) >= 0 ? 1.0 : 0.3))

      const percentage = ((100 * d.value) / root.value).toPrecision(3)
      label
        .style('visibility', null)
        .select('.percentage')
        .text(percentage + ' %')
    })
}
</script>

<template>
  <v-container class="summary">
    <div id="sunburst"></div>
  </v-container>
</template>

<style scoped>
.summary {
  margin: 0 30px 0 60px;
  padding: 0;
}
</style>
