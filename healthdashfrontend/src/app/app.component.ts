import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router'; // ✅ import this

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet], // ✅ add this
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  isSidebarCollapsed = false;

  toggleSidebar() {
    this.isSidebarCollapsed = !this.isSidebarCollapsed;
  }
}
