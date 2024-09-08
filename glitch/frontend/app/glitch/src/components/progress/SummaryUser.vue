<script setup lang="ts">
import { ref, defineProps, watch } from 'vue'

import type { SummaryItem } from '@/types/Summary'
import useProgressStore from '@/stores/ProgressStore'

// @ts-ignore
import * as d3 from 'd3'

const props = defineProps<{
  rid_users: number
}>()

const store_progress = useProgressStore()

const value_workload = ref(0)
const value_number = ref(0)
const value_bug = ref(0)
const value_risk_alert = ref(0)

enum SummaryType {
  NONE = 0,
  WORKLOAD,
  NUMBER,
  BUG,
  RISK_ALERT
}

watch(
  () => store_progress.summaries_user.get(props.rid_users),
  () => {
    createChart()
  }
)

function createChart() {
  const list_data = store_progress.summaries_user.get(props.rid_users)
  if (!list_data || list_data.length === 0) {
    return
  }

  const max_value = d3.max(list_data, (d: SummaryItem) =>
    Math.max(d.task_count_complete + d.bug_count_complete, d.task_count_total + d.bug_count_total)
  ) as number
  const max_value_number = d3.max(list_data, (d: SummaryItem) =>
    Math.max(d.task_number_total)
  ) as number

  if (max_value == 0 && max_value_number == 0) {
    return
  }

  d3.select(`#graph-workload`).selectAll('svg').remove()
  d3.select(`#graph-number`).selectAll('svg').remove()
  d3.select(`#graph-bug`).selectAll('svg').remove()
  d3.select(`#graph-risk-alert`).selectAll('svg').remove()

  const latest = list_data[list_data.length - 1]
  value_workload.value = Math.floor((latest.task_count_complete / latest.task_count_total) * 100)
  value_number.value = Math.floor((latest.task_number_completed / latest.task_number_total) * 100)
  value_bug.value = Math.floor((latest.bug_count_complete / latest.bug_count_total) * 100)
  value_risk_alert.value = latest.task_count_alert + latest.bug_count_alert

  createChartTypeWorkload(SummaryType.WORKLOAD, list_data, max_value)
  createChartTypeWorkload(SummaryType.NUMBER, list_data, max_value_number)
  createChartTypeWorkload(SummaryType.BUG, list_data, max_value)
  createChartTypeWorkload(SummaryType.RISK_ALERT, list_data, max_value)
}

function createChartTypeWorkload(type: SummaryType, data: SummaryItem[], max_value: number) {
  const date_end = d3.max(data, (d: any) => new Date(d.date_entry)) as Date
  const date_start = new Date(date_end)
  date_start.setDate(date_end.getDate() - 21)

  const width = 270
  const height = 110

  const x = d3.scaleTime().domain([date_start, date_end]).range([0, width])
  const y = d3
    .scaleLinear()
    .domain([0, max_value + 2])
    .nice()
    .range([height, 0])

  let svg: any
  let list_area: any[] = []

  switch (type) {
    case SummaryType.WORKLOAD:
      svg = d3.select(`#graph-workload`).append('svg')
      list_area = [
        {
          name: 'Total',
          value: (d: SummaryItem) => d.task_count_total,
          color_line: 'rgba(116, 119, 176, 0.9)',
          color_area: 'rgba(116, 119, 176, 0.2)'
        },
        {
          name: 'Complete',
          value: (d: SummaryItem) => d.task_count_complete,
          color_line: 'rgba(90, 90, 90, 0.9)',
          color_area: 'rgba(90, 90, 90, 0.7)'
        }
      ]
      break

    case SummaryType.NUMBER:
      svg = d3.select(`#graph-number`).append('svg')
      list_area = [
        {
          name: 'Total',
          value: (d: SummaryItem) => d.task_number_total,
          color_line: 'rgba(98, 163, 136, 0.9)',
          color_area: 'rgba(98, 163, 136, 0.2)'
        },
        {
          name: 'Complete',
          value: (d: SummaryItem) => d.task_number_completed,
          color_line: 'rgba(90, 90, 90, 0.9)',
          color_area: 'rgba(90, 90, 90, 0.7)'
        }
      ]
      break

    case SummaryType.BUG:
      svg = d3.select(`#graph-bug`).append('svg')
      list_area = [
        {
          name: 'Total',
          value: (d: SummaryItem) => d.bug_count_total,
          color_line: 'rgba(120, 92, 10, 0.9)',
          color_area: 'rgba(120, 92, 10, 0.2)'
        },
        {
          name: 'Complete',
          value: (d: SummaryItem) => d.bug_count_complete,
          color_line: 'rgba(90, 90, 90, 0.9)',
          color_area: 'rgba(90, 90, 90, 0.7)'
        }
      ]
      break

    case SummaryType.RISK_ALERT:
      svg = d3.select(`#graph-risk-alert`).append('svg')
      list_area = [
        {
          name: 'Risk',
          value: (d: SummaryItem) => d.task_risk + d.bug_risk,
          color_line: 'rgba(156, 145, 81, 0.9)',
          color_area: 'rgba(156, 145, 81, 0.2)'
        },
        {
          name: 'Alert',
          value: (d: SummaryItem) => d.task_count_alert + d.bug_count_alert,
          color_line: 'rgba(181, 48, 69, 0.9)',
          color_area: 'rgba(181, 48, 69, 0.2)'
        }
      ]
      break
  }

  svg.attr('width', width).attr('height', height).append('g')

  list_area.forEach((area) => {
    const areaPath = d3
      .area<SummaryItem>()
      .x((d: any) => x(new Date(d.date_entry)))
      .y0(y(0))
      .y1((d: any) => y(area.value(d)))
      .curve(d3.curveMonotoneX)

    svg.append('path').datum(data).attr('fill', area.color_area).attr('d', areaPath)

    const linePath = d3
      .line<SummaryItem>()
      .x((d: any) => x(new Date(d.date_entry)))
      .y((d: any) => y(area.value(d)))
      .curve(d3.curveMonotoneX)

    svg
      .append('path')
      .datum(data)
      .attr('fill', 'none')
      .attr('stroke', area.color_line)
      .attr('stroke-width', 1.2)
      .attr('d', linePath)
  })

  svg
    .append('g')
    .call(
      d3.axisBottom(x).ticks(d3.timeDay.every(1)).tickFormat(d3.timeFormat('%m-%d')).tickSize(0)
    )
    .attr('transform', `translate(0,${height})`)
    .attr('color', '#393939')
    .attr('stroke-width', 2.5)
    .selectAll('text')
    .style('display', 'none')
}
</script>

<template>
  <v-container class="summary">
    <v-row>
      <v-col cols="auto" class="d-flex summary-block">
        <v-card class="flex-grow-1">
          <v-card-text>
            <div class="title-sub">completed rate</div>
            <div class="title">
              <span>Type : Workload</span>
              <span class="value" v-if="!isNaN(value_workload)">{{ value_workload }} %</span>
              <span class="value" v-else>-</span>
            </div>
            <div class="graph" :id="`graph-workload`"></div>
          </v-card-text>
        </v-card>
      </v-col>

      <v-col cols="auto" class="d-flex summary-block">
        <v-card class="flex-grow-1">
          <v-card-text>
            <div class="title-sub">completed rate</div>
            <div class="title">
              <span>Type : Number</span>
              <span class="value" v-if="!isNaN(value_number)">{{ value_number }} %</span>
              <span class="value" v-else>-</span>
            </div>
            <div class="graph" :id="`graph-number`"></div>
          </v-card-text>
        </v-card>
      </v-col>

      <v-col cols="auto" class="d-flex summary-block">
        <v-card class="flex-grow-1">
          <v-card-text>
            <div class="title-sub">completed rate</div>
            <div class="title">
              <span>Bug</span>
              <span class="value" v-if="!isNaN(value_bug)">{{ value_bug }} %</span>
              <span class="value" v-else>-</span>
            </div>
            <div class="graph" :id="`graph-bug`"></div>
          </v-card-text>
        </v-card>
      </v-col>

      <v-col cols="auto" class="d-flex summary-block">
        <v-card class="flex-grow-1">
          <v-card-text>
            <div class="title-sub">caution</div>
            <div class="title">
              <span>Risk & Alert</span>
              <span class="value" v-if="!isNaN(value_risk_alert)">
                {{ value_risk_alert }} alert
              </span>
              <span class="value" v-else>-</span>
            </div>
            <div class="graph" :id="`graph-risk-alert`"></div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped>
.summary {
  margin: 0 0 0 32px;
  padding: 0;
}

.summary-block {
  margin: 5px 10px 0 0;
  padding: 10px 0 0 0;
}

.title-sub {
  font-size: 14px;
  color: #797979;
}

.title {
  font-size: 20px;
  font-weight: bold;
  color: #acacac;
}

.value {
  position: absolute;
  top: 27px;
  right: 34px;
  font-size: 28px;
  color: #cfcfcf;
}

.graph {
  margin: 10px 10px 0 0;
  padding: 0;
  background-color: #070707;
}
</style>
