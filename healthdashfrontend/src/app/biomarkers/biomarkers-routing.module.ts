import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BiomarkersComponent } from './biomarkers.component';

const routes: Routes = [{ path: '', component: BiomarkersComponent }];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class BiomarkersRoutingModule { }
