import { Routes } from '@angular/router';
import { DashComponent } from './dash/dash.component'
import { UploadComponent } from './upload/upload.component';

export const routes: Routes = [
  { path: 'dash', component: DashComponent },
  { path: 'upload', component: UploadComponent },
  { path: '', redirectTo: 'dash', pathMatch: 'full' }
];