import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

export type TileType = 'timeline' | 'static' | 'dynamic';
export type DisplayType = 'circle' | 'bar' | 'icon' | 'number';

export interface TileData {
  title: string;
  value: number | string;
  icon?: string;
  color?: string;
  source?: string;
  groupId?: string;
  displayType?: DisplayType;
}

@Component({
  selector: 'app-base-tile',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div class="tile" [ngClass]="{'grouped': data.groupId}" [style.background-color]="data.color">
      <div class="tile-header">
        <h3>{{ data.title }}</h3>
        <span *ngIf="data.source" class="source">{{ data.source }}</span>
      </div>
      <div class="tile-content">
        <ng-content></ng-content>
      </div>
    </div>
  `,
  styles: [`
    .tile {
      background: white;
      border-radius: 12px;
      padding: 1rem;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
      height: 100%;
      display: flex;
      flex-direction: column;
    }

    .tile-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1rem;
    }

    .tile-header h3 {
      margin: 0;
      font-size: 1rem;
      color: #333;
    }

    .source {
      font-size: 0.8rem;
      color: #666;
    }

    .tile-content {
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .grouped {
      border: 2px solid rgba(255,255,255,0.2);
    }
  `]
})
export class BaseTileComponent {
  @Input() data!: TileData;
  @Input() type!: TileType;
} 