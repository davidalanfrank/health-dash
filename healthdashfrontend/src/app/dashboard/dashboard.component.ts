import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { StaticTileComponent } from '../shared/components/static-tile/static-tile.component';
import { TimelineTileComponent, TimeSeriesData } from '../shared/components/timeline-tile/timeline-tile.component';
import { DynamicTileComponent } from '../shared/components/dynamic-tile/dynamic-tile.component';
import { TileData } from '../shared/components/base-tile/base-tile.component';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [
    CommonModule,
    StaticTileComponent,
    TimelineTileComponent,
    DynamicTileComponent
  ],
  template: `
    <div class="dashboard">
      <div class="dashboard-grid">
        <!-- Sleep Metrics Group -->
        <div class="tile-group" style="background-color: rgba(76, 175, 80, 0.1);">
          <h2>Sleep Metrics</h2>
          <div class="group-tiles">
            <app-static-tile
              [data]="sleepScoreData"
              class="tile">
            </app-static-tile>
            
            <app-timeline-tile
              [data]="sleepDurationData"
              [timeSeriesData]="sleepDurationTimeSeries"
              class="tile">
            </app-timeline-tile>
          </div>
        </div>

        <!-- Activity Metrics Group -->
        <div class="tile-group" style="background-color: rgba(33, 150, 243, 0.1);">
          <h2>Activity Metrics</h2>
          <div class="group-tiles">
            <app-dynamic-tile
              [data]="heartRateData"
              [webhookUrl]="heartRateWebhookUrl"
              class="tile">
            </app-dynamic-tile>
            
            <app-static-tile
              [data]="stepsData"
              class="tile">
            </app-static-tile>
          </div>
        </div>

        <!-- Nutrition Metrics Group -->
        <div class="tile-group" style="background-color: rgba(255, 152, 0, 0.1);">
          <h2>Nutrition Metrics</h2>
          <div class="group-tiles">
            <app-static-tile
              [data]="waterIntakeData"
              class="tile">
            </app-static-tile>
            
            <app-timeline-tile
              [data]="calorieData"
              [timeSeriesData]="calorieTimeSeries"
              class="tile">
            </app-timeline-tile>
          </div>
        </div>
      </div>
    </div>
  `,
  styles: [`
    .dashboard {
      padding: 2rem;
      min-height: 100vh;
      background-color: #f5f5f5;
    }

    .dashboard-grid {
      display: grid;
      gap: 2rem;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    }

    .tile-group {
      padding: 1.5rem;
      border-radius: 16px;
    }

    .tile-group h2 {
      margin: 0 0 1rem 0;
      font-size: 1.5rem;
      color: #333;
    }

    .group-tiles {
      display: grid;
      gap: 1rem;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    }

    .tile {
      min-height: 200px;
    }
  `]
})
export class DashboardComponent implements OnInit {
  // Sleep Metrics
  sleepScoreData: TileData = {
    title: 'Sleep Score',
    value: 85,
    displayType: 'circle',
    source: 'Fitbit',
    groupId: 'sleep'
  };

  sleepDurationData: TileData = {
    title: 'Sleep Duration',
    value: '7.5h',
    source: 'Fitbit',
    groupId: 'sleep'
  };

  sleepDurationTimeSeries: TimeSeriesData[] = [
    // Add your time series data here
  ];

  // Activity Metrics
  heartRateData: TileData = {
    title: 'Heart Rate',
    value: '72',
    icon: 'fas fa-heartbeat',
    source: 'Apple Watch',
    groupId: 'activity'
  };

  heartRateWebhookUrl = 'your-heart-rate-webhook-url';

  stepsData: TileData = {
    title: 'Daily Steps',
    value: 8500,
    displayType: 'bar',
    source: 'Apple Watch',
    groupId: 'activity'
  };

  // Nutrition Metrics
  waterIntakeData: TileData = {
    title: 'Water Intake',
    value: 2.5,
    displayType: 'icon',
    icon: 'fas fa-tint',
    source: 'Health App',
    groupId: 'nutrition'
  };

  calorieData: TileData = {
    title: 'Calories',
    value: '2000',
    source: 'Health App',
    groupId: 'nutrition'
  };

  calorieTimeSeries: TimeSeriesData[] = [
    // Add your time series data here
  ];

  ngOnInit() {
    // Initialize any necessary data or services
  }
}
