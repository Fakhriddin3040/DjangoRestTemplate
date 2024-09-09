import { Component } from '@angular/core';
import { ContainerComponent } from '../../shared/container/container.component';
import { Section1ProductSlideComponent } from "./section1-product-slide/section1-product-slide.component";
import { Section2OurAdvantagesComponent } from "./section2-our-advantages/section2-our-advantages.component";

@Component({
  selector: 'app-main',
  standalone: true,
  imports: [
    ContainerComponent,
    Section1ProductSlideComponent,
    Section2OurAdvantagesComponent
],
  templateUrl: './main.component.html',
  styleUrl: './main.component.scss'
})
export class MainComponent {

}
