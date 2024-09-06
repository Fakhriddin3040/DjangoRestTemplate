import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HeaderComponent } from './layout/header/header.component';
import { MainComponent } from "./layout/main/main.component";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, HeaderComponent, MainComponent],
  templateUrl: './app.component.html',  
  styleUrls: ['./app.component.scss'],   
})
export class AppComponent {
  title = 'marketplace-client';
}
