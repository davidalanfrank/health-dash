import { Component, Input, OnInit, OnDestroy } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BaseTileComponent, TileData } from '../base-tile/base-tile.component';
import { Subject } from 'rxjs';
import { takeUntil } from 'rxjs/operators';

@Component({
  selector: 'app-dynamic-tile',
  standalone: true,
  imports: [CommonModule, BaseTileComponent],
  template: `
    <app-base-tile [data]="data" type="dynamic">
      <div class="dynamic-content">
        <div class="value-display">
          {{ currentValue }}
        </div>
        <div class="update-time" *ngIf="lastUpdateTime">
          Last updated: {{ lastUpdateTime | date:'shortTime' }}
        </div>
      </div>
    </app-base-tile>
  `,
  styles: [`
    .dynamic-content {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.5rem;
    }

    .value-display {
      font-size: 2rem;
      font-weight: bold;
    }

    .update-time {
      font-size: 0.8rem;
      color: #666;
    }
  `]
})
export class DynamicTileComponent implements OnInit, OnDestroy {
  @Input() data!: TileData;
  @Input() webhookUrl!: string;

  currentValue: number | string = 0;
  lastUpdateTime: Date | null = null;
  private destroy$ = new Subject<void>();

  ngOnInit() {
    this.initializeWebhook();
  }

  ngOnDestroy() {
    this.destroy$.next();
    this.destroy$.complete();
  }

  private initializeWebhook() {
    // Here you would typically set up your webhook connection
    // This is a placeholder for the actual webhook implementation
    const eventSource = new EventSource(this.webhookUrl);

    eventSource.onmessage = (event) => {
      const data = JSON.parse(event.data);
      this.updateValue(data.value);
    };

    eventSource.onerror = (error) => {
      console.error('Webhook error:', error);
      eventSource.close();
    };
  }

  private updateValue(newValue: number | string) {
    this.currentValue = newValue;
    this.lastUpdateTime = new Date();
  }
} 