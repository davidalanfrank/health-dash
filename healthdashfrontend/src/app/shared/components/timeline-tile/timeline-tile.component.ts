import { Component, Input, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BaseTileComponent, TileData } from '../base-tile/base-tile.component';
import { NgxChartsModule } from '@swimlane/ngx-charts';

export interface TimeSeriesData {
  name: string;
  value: number;
  date: Date;
}

@Component({
  selector: 'app-timeline-tile',
  standalone: true,
  imports: [CommonModule, BaseTileComponent, NgxChartsModule],
  template: `
    <app-base-tile [data]="data" type="timeline">
      <div class="timeline-content">
        <ngx-charts-line-chart
          [results]="chartData"
          [gradient]="true"
          [xAxis]="true"
          [yAxis]="true"
          [legend]="false"
          [showXAxisLabel]="false"
          [showYAxisLabel]="false"
          [autoScale]="true"
          [timeline]="false"
          [scheme]="'cool'"
          [animations]="true">
        </ngx-charts-line-chart>
      </div>
    </app-base-tile>
  `,
  styles: [`
    .timeline-content {
      width: 100%;
      height: 100%;
      min-height: 200px;
    }
  `]
})
export class TimelineTileComponent implements OnInit {
  @Input() data!: TileData;
  @Input() timeSeriesData: TimeSeriesData[] = [];

  chartData: any[] = [];

  ngOnInit() {
    this.prepareChartData();
  }

  private prepareChartData() {
    // Group data by month
    const monthlyData = this.timeSeriesData.reduce((acc, curr) => {
      const month = new Date(curr.date).toLocaleString('default', { month: 'short' });
      if (!acc[month]) {
        acc[month] = [];
      }
      acc[month].push(curr.value);
      return acc;
    }, {} as { [key: string]: number[] });

    // Calculate averages and format for chart
    this.chartData = [{
      name: this.data.title,
      series: Object.entries(monthlyData).map(([month, values]) => ({
        name: month,
        value: values.reduce((a, b) => a + b, 0) / values.length
      }))
    }];
  }
} 