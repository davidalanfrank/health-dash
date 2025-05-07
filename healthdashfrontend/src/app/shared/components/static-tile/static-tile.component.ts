import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BaseTileComponent, TileData, DisplayType } from '../base-tile/base-tile.component';

@Component({
  selector: 'app-static-tile',
  standalone: true,
  imports: [CommonModule, BaseTileComponent],
  template: `
    <app-base-tile [data]="data" type="static">
      <div class="static-content" [ngSwitch]="data.displayType">
        <!-- Circle Display -->
        <div *ngSwitchCase="'circle'" class="circle-display">
          <div class="circle-progress" [style.--progress]="getProgressValue()">
            <div class="circle-value">{{ data.value }}</div>
          </div>
        </div>

        <!-- Bar Display -->
        <div *ngSwitchCase="'bar'" class="bar-display">
          <div class="bar-progress" [style.width.%]="getProgressValue()">
            <span class="bar-value">{{ data.value }}</span>
          </div>
        </div>

        <!-- Icon Display -->
        <div *ngSwitchCase="'icon'" class="icon-display">
          <i [class]="data.icon"></i>
          <span class="icon-value">{{ data.value }}</span>
        </div>

        <!-- Number Display -->
        <div *ngSwitchCase="'number'" class="number-display">
          {{ data.value }}
        </div>
      </div>
    </app-base-tile>
  `,
  styles: [`
    .static-content {
      width: 100%;
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .circle-display {
      position: relative;
      width: 120px;
      height: 120px;
    }

    .circle-progress {
      width: 100%;
      height: 100%;
      border-radius: 50%;
      background: conic-gradient(
        var(--tile-color, #4CAF50) calc(var(--progress) * 1%),
        #e0e0e0 calc(var(--progress) * 1%)
      );
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .circle-progress::before {
      content: '';
      position: absolute;
      width: 80%;
      height: 80%;
      background: white;
      border-radius: 50%;
    }

    .circle-value {
      position: relative;
      font-size: 1.5rem;
      font-weight: bold;
    }

    .bar-display {
      width: 100%;
      height: 40px;
      background: #e0e0e0;
      border-radius: 20px;
      overflow: hidden;
    }

    .bar-progress {
      height: 100%;
      background: var(--tile-color, #4CAF50);
      display: flex;
      align-items: center;
      justify-content: center;
      transition: width 0.3s ease;
    }

    .bar-value {
      color: white;
      font-weight: bold;
    }

    .icon-display {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.5rem;
    }

    .icon-display i {
      font-size: 2rem;
      color: var(--tile-color, #4CAF50);
    }

    .icon-value {
      font-size: 1.5rem;
      font-weight: bold;
    }

    .number-display {
      font-size: 2.5rem;
      font-weight: bold;
    }
  `]
})
export class StaticTileComponent {
  @Input() data!: TileData;

  getProgressValue(): number {
    if (typeof this.data.value === 'number') {
      return Math.min(Math.max(this.data.value, 0), 100);
    }
    return 0;
  }
} 