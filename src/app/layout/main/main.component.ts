import { Component } from '@angular/core';
import { ContainerComponent } from '../../shared/container/container.component';

@Component({
  selector: 'app-main',
  standalone: true,
  imports: [ContainerComponent],
  templateUrl: './main.component.html',
  styleUrl: './main.component.scss'
})
export class MainComponent {

}
