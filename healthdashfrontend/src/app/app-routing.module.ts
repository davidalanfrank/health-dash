import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  { path: 'dashboard', loadChildren: () => import('./dashboard/dashboard.module').then(m => m.DashboardModule) },
  { path: 'upload', loadChildren: () => import('./upload/upload.module').then(m => m.UploadModule) },
  { path: 'biomarkers', loadChildren: () => import('./biomarkers/biomarkers.module').then(m => m.BiomarkersModule) },
  { path: 'reports', loadChildren: () => import('./reports/reports.module').then(m => m.ReportsModule) }, 
  { path: '', redirectTo: '/dashboard', pathMatch: 'full' },
  { path: 'data', loadChildren: () => import('./data/data.module').then(m => m.DataModule) },// redirect to `dashboard` route by default
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }