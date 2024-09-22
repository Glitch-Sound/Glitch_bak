<script setup lang="ts">
import { ref, onMounted, defineProps, watch } from 'vue'

import type { Item } from '@/types/Item'
import type { SummaryItem } from '@/types/Summary'
import useSummaryStore from '@/stores/SummaryStore'

// @ts-ignore
import * as d3 from 'd3'

const props = defineProps<{
  item: Item
}>()

const store_summary = useSummaryStore()

const is_enable = ref(false)

const is_enable_workload = ref(false)
const is_enable_number = ref(false)
const is_enable_bug = ref(false)
const is_enable_alert = ref(false)

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

onMounted(async () => {
  await store_summary.fetchSummaryItem(props.item.rid)
  createChart()
})

watch(
  () => store_summary.summaries_item.get(props.item.rid),
  () => {
    createChart()
  }
)

function createChart() {
  const list_data = store_summary.summaries_item.get(props.item.rid)
  if (!list_data || list_data.length === 0) {
    return
  }

  const max_value_count = d3.max(list_data, (d: SummaryItem) =>
    Math.max(d.task_count_total + d.bug_count_total)
  ) as number
  const max_value_number = d3.max(list_data, (d: SummaryItem) =>
    Math.max(d.task_number_total)
  ) as number
  const max_value_bug = d3.max(list_data, (d: SummaryItem) => Math.max(d.bug_count_total)) as number
  const max_value_alert = d3.max(list_data, (d: SummaryItem) =>
    Math.max(d.task_count_alert + d.bug_count_alert)
  ) as number

  is_enable.value = true

  if (max_value_count != 0) {
    is_enable_workload.value = true
  }

  if (max_value_number != 0) {
    is_enable_number.value = true
  }

  if (max_value_bug != 0) {
    is_enable_bug.value = true
  }

  if (max_value_alert != 0) {
    is_enable_alert.value = true
  }

  d3.select(`#graph-workload-${props.item.rid}`).selectAll('svg').remove()
  d3.select(`#graph-number-${props.item.rid}`).selectAll('svg').remove()
  d3.select(`#graph-bug-${props.item.rid}`).selectAll('svg').remove()
  d3.select(`#graph-risk-alert-${props.item.rid}`).selectAll('svg').remove()

  const latest = list_data[list_data.length - 1]
  value_workload.value = Math.floor((latest.task_count_complete / latest.task_count_total) * 100)
  value_number.value = Math.floor((latest.task_number_completed / latest.task_number_total) * 100)
  value_bug.value = Math.floor((latest.bug_count_complete / latest.bug_count_total) * 100)
  value_risk_alert.value = latest.task_count_alert + latest.bug_count_alert

  createChartDetail(SummaryType.WORKLOAD, list_data, max_value_count)
  createChartDetail(SummaryType.NUMBER, list_data, max_value_number)
  createChartDetail(SummaryType.BUG, list_data, max_value_bug)
  createChartDetail(SummaryType.RISK_ALERT, list_data, max_value_alert)
}

function createChartDetail(type: SummaryType, data: SummaryItem[], max_values: number) {
  const date_end = d3.max(data, (d: any) => new Date(d.date_entry)) as Date
  const date_start = new Date(date_end)
  date_start.setDate(date_end.getDate() - 21)

  const width = 270
  const height = 80

  const x = d3.scaleTime().domain([date_start, date_end]).range([0, width])

  let svg: any
  let list_area: any[] = []
  let yScales: any[] = []

  switch (type) {
    case SummaryType.WORKLOAD: {
      svg = d3.select(`#graph-workload-${props.item.rid}`).append('svg')
      const y_workload = d3
        .scaleLinear()
        .domain([0, (max_values as number) + 2])
        .nice()
        .range([height, 0])
      yScales = [y_workload, y_workload]
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
    }
    case SummaryType.NUMBER: {
      svg = d3.select(`#graph-number-${props.item.rid}`).append('svg')
      const y_number = d3
        .scaleLinear()
        .domain([0, (max_values as number) + 2])
        .nice()
        .range([height, 0])
      yScales = [y_number, y_number]
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
    }
    case SummaryType.BUG: {
      svg = d3.select(`#graph-bug-${props.item.rid}`).append('svg')
      const y_bug = d3
        .scaleLinear()
        .domain([0, (max_values as number) + 2])
        .nice()
        .range([height, 0])
      yScales = [y_bug, y_bug]
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
    }
    case SummaryType.RISK_ALERT: {
      svg = d3.select(`#graph-risk-alert-${props.item.rid}`).append('svg')
      const y_risk = d3.scaleLinear().domain([0, 1100]).nice().range([height, 0])
      const y_alert = d3
        .scaleLinear()
        .domain([0, (max_values as number) + 2])
        .nice()
        .range([height, 0])
      yScales = [y_risk, y_alert]
      list_area = [
        {
          name: 'Risk',
          value: (d: SummaryItem) => d.risk,
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
    default:
      break
  }

  svg.attr('width', width).attr('height', height).append('g')

  list_area.forEach((area, index) => {
    const yScale = yScales[index]

    const areaPath = d3
      .area<SummaryItem>()
      .x((d: any) => x(new Date(d.date_entry)))
      .y0(yScale(0))
      .y1((d: any) => yScale(area.value(d)))
      .curve(d3.curveLinear)

    svg.append('path').datum(data).attr('fill', area.color_area).attr('d', areaPath)

    const linePath = d3
      .line<SummaryItem>()
      .x((d: any) => x(new Date(d.date_entry)))
      .y((d: any) => yScale(area.value(d)))
      .curve(d3.curveLinear)

    svg
      .append('path')
      .datum(data)
      .attr('fill', 'none')
      .attr('stroke', area.color_line)
      .attr('stroke-width', 1.2)
      .attr('d', linePath)
  })

  if (type === SummaryType.RISK_ALERT) {
    svg
      .append('g')
      .call(d3.axisLeft(yScales[0]).ticks(5))
      .attr('color', '#393939')
      .attr('stroke-width', 1)
    svg
      .append('g')
      .call(d3.axisRight(yScales[1]).ticks(5))
      .attr('transform', `translate(${width},0)`)
      .attr('color', '#393939')
      .attr('stroke-width', 1)
  } else {
    svg
      .append('g')
      .call(d3.axisLeft(yScales[0]).ticks(5))
      .attr('color', '#393939')
      .attr('stroke-width', 1)
  }

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
  <v-container class="summary" v-if="is_enable">
    <v-row>
      <v-col cols="auto" class="d-flex summary-block">
        <v-card class="flex-grow-1">
          <v-card-text>
            <div class="title-sub">completed rate</div>
            <div class="title">
              <span>Type : Workload</span>
              <span class="value" v-if="is_enable_workload">{{ value_workload }} %</span>
              <span class="value" v-else>-</span>
            </div>
            <div class="graph" :id="`graph-workload-${props.item.rid}`"></div>
          </v-card-text>
        </v-card>
      </v-col>

      <v-col cols="auto" class="d-flex summary-block">
        <v-card class="flex-grow-1">
          <v-card-text>
            <div class="title-sub">completed rate</div>
            <div class="title">
              <span>Type : Number</span>
              <span class="value" v-if="is_enable_number">{{ value_number }} %</span>
              <span class="value" v-else>-</span>
            </div>
            <div class="graph" :id="`graph-number-${props.item.rid}`"></div>
          </v-card-text>
        </v-card>
      </v-col>

      <v-col cols="auto" class="d-flex summary-block">
        <v-card class="flex-grow-1">
          <v-card-text>
            <div class="title-sub">completed rate</div>
            <div class="title">
              <span>Bug</span>
              <span class="value" v-if="is_enable_bug">{{ value_bug }} %</span>
              <span class="value" v-else>-</span>
            </div>
            <div class="graph" :id="`graph-bug-${props.item.rid}`"></div>
          </v-card-text>
        </v-card>
      </v-col>

      <v-col cols="auto" class="d-flex summary-block">
        <v-card class="flex-grow-1">
          <v-card-text>
            <div class="title-sub">caution</div>
            <div class="title">
              <span>Risk & Alert</span>
              <span class="value" v-if="is_enable_alert"> {{ value_risk_alert }} alert </span>
              <span class="value" v-else>-</span>
            </div>
            <div class="graph" :id="`graph-risk-alert-${props.item.rid}`"></div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped>
.summary {
  margin: 0 0 0 65px;
  padding: 0;
}

.summary-block {
  margin: 10px 10px 0 0;
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
