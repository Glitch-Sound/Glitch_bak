<script setup lang="ts">
import { onMounted, ref } from 'vue'
import * as d3 from 'd3'

import useSummaryStore from '@/stores/SummaryStore'
import useAnalyzeStore from '@/stores/AnalyzeStore'

const props = defineProps<{
  id_project: number | null
}>()

const store_analyze = useAnalyzeStore()
const store_summary = useSummaryStore()

const selectedData = ref('')

onMounted(async () => {
  await store_analyze.fetchItemsFrequency(props.id_project)
  await store_summary.fetchSummaryProject(props.id_project)
  createCalendar()

  if (d3.select('#chart').node()) {
    createChart()
    updateChart()
  }
})

function createCalendar() {
  const cellSize = 17
  const radius = 4
  const width = 53 * cellSize
  const height = 7 * cellSize

  const svg = d3
    .select('#calendar')
    .append('svg')
    .attr('width', width)
    .attr('height', height + 20)
    .append('g')
    .attr('transform', `translate(20,20)`)

  const timeFormat = d3.timeFormat('%Y-%m-%d')

  const endDate = new Date(2024, 8, 30)
  const startDate = new Date(endDate.getFullYear() - 1, endDate.getMonth(), 1)
  const days = d3.timeDays(startDate, endDate)

  const taskColors = ['rgba(0, 0, 255, 0.3)', 'rgba(0, 0, 255, 0.9)']
  const bugColors = ['rgba(255, 0, 0, 0.3)', 'rgba(255, 0, 0, 0.9)']

  const maxTask = d3.max(store_analyze.items_frequency, (d) => d.task_count)
  const maxBug = d3.max(store_analyze.items_frequency, (d) => d.bug_count)

  const taskColorScale = d3
    .scaleQuantize()
    .domain([0, maxTask || 1])
    .range(taskColors)
  const bugColorScale = d3
    .scaleQuantize()
    .domain([0, maxBug || 1])
    .range(bugColors)

  svg
    .selectAll('rect')
    .data(days)
    .enter()
    .append('rect')
    .attr('width', cellSize)
    .attr('height', cellSize)
    .attr('x', (d) => {
      const startDate = new Date(2023, 9, 1)
      const weekCount = d3.timeWeek.count(startDate, d)
      return weekCount * cellSize
    })
    .attr('y', (d) => d.getDay() * cellSize)
    .attr('rx', radius)
    .attr('ry', radius)
    .attr('fill', (d) => {
      const date = timeFormat(d)
      const data = store_analyze.items_frequency.find((item) => {
        const itemDate = item.datetime_entry.split(' ')[0]
        return itemDate === date
      })

      if (data) {
        if (data.task_count > 0 && data.bug_count > 0) {
          const taskColor = d3.color(taskColorScale(data.task_count))!.rgb()
          const bugColor = d3.color(bugColorScale(data.bug_count))!.rgb()
          const blendedColor = d3.rgb(
            taskColor.r * 0.3 + bugColor.r * 0.7,
            taskColor.g * 0.3 + bugColor.g * 0.7,
            taskColor.b * 0.3 + bugColor.b * 0.7
          )
          return blendedColor.toString()
        } else if (data.bug_count > 0) {
          return bugColorScale(data.bug_count)
        } else if (data.task_count > 0) {
          return taskColorScale(data.task_count)
        }
      }
      return '#0f0f0f'
    })
    .attr('stroke', '#000000')
    .attr('stroke-width', 1.5)
    .style('opacity', 0.8)
    .on('mouseover', (event, d) => {
      const date = timeFormat(d)
      selectedData.value = store_summary.summaries_project.find(
        (summary) => summary.date_entry === date
      )

      updateChart()
    })
}

function createChart() {
  const width = 300
  const height = 300
  const innerRadius = 50
  const outerRadius = 100

  const svg = d3
    .select('#chart')
    .append('svg')
    .attr('width', width)
    .attr('height', height)
    .append('g')
    .attr('transform', `translate(${width / 2}, ${height / 2})`)

  svg.append('g').attr('class', 'innerPie')
  svg.append('g').attr('class', 'outerPie')

  updateChart(svg, innerRadius, outerRadius)
}

function updateChart(svg = null, innerRadius = 50, outerRadius = 100) {
  const data = selectedData.value

  if (!data) {
    d3.select('#chart').selectAll('path').remove()
    d3.select('#chart')
      .select('.innerPie')
      .append('text')
      .attr('text-anchor', 'middle')
      .attr('fill', 'gray')
    return
  }

  // 内側のデータ (task_count_total, bug_count_total)
  const innerData = [
    { label: 'Task', value: data.task_count_total },
    { label: 'Bug', value: data.bug_count_total }
  ]

  // 外側のデータ (詳細ステータス)
  const outerData = [
    { label: 'Task Idle', value: data.task_count_idle },
    { label: 'Task Run', value: data.task_count_run },
    { label: 'Task Alert', value: data.task_count_alert },
    { label: 'Task Review', value: data.task_count_review },
    { label: 'Task Complete', value: data.task_count_complete },
    { label: 'Bug Idle', value: data.bug_count_idle },
    { label: 'Bug Run', value: data.bug_count_run },
    { label: 'Bug Alert', value: data.bug_count_alert },
    { label: 'Bug Review', value: data.bug_count_review },
    { label: 'Bug Complete', value: data.bug_count_complete }
  ]

  // 色の定義
  const innerColors = ['#1f77b4', '#ff7f0e'] // 内側：タスク（青）、バグ（オレンジ）
  const outerColors = {
    task: ['#aec7e8', '#ffbb78', '#2ca02c', '#d62728', '#9467bd'], // タスク詳細色
    bug: ['#f28e2b', '#e15759', '#76b7b2', '#59a14f', '#edc949'] // バグ詳細色
  }

  // Pieのソートを無効化して定義順に表示
  const pie = d3
    .pie()
    .value((d: any) => d.value)
    .sort(null)

  // 内側と外側のドーナツの半径設定
  const innerArc = d3
    .arc()
    .innerRadius(innerRadius - 20)
    .outerRadius(innerRadius) // 内側もドーナツ状に
  const outerArc = d3
    .arc()
    .innerRadius(innerRadius + 10)
    .outerRadius(outerRadius)

  // 内側のドーナツチャート更新
  d3.select('#chart')
    .select('.innerPie')
    .selectAll('path')
    .data(pie(innerData))
    .join('path')
    .attr('d', innerArc)
    .attr('fill', (d, i) => innerColors[i]) // タスクとバグの色を定義

  // 外側のドーナツチャート更新
  d3.select('#chart')
    .select('.outerPie')
    .selectAll('path')
    .data(pie(outerData))
    .join('path')
    .attr('d', outerArc)
    .attr('fill', (d, i) => {
      // タスクの色かバグの色かを条件で判定
      return i < 5 ? outerColors.task[i] : outerColors.bug[i - 5]
    })
}
</script>

<template>
  <div class="container">
    <div id="calendar"></div>
    <div id="chart"></div>
  </div>
</template>

<style scoped>
.container {
  display: flex; /* 横並びにする */
  justify-content: space-between; /* 両側に余白を設定して分割 */
  align-items: flex-start; /* 上側を揃える */
}

#calendar,
#chart {
  flex: 1; /* 横幅を同じ割合で分割 */
  margin: 10px; /* 要素間に少し余白を追加 */
}

svg {
  font-family: sans-serif;
}
</style>
