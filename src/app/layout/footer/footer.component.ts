import { Component } from '@angular/core';
import { ContainerComponent } from '../../shared/container/container.component';
import { FooterSection1SubscribeComponent } from './footer-section1-subscribe/footer-section1-subscribe.component';
import { FooterSection2ContactComponent } from './footer-section2-contact/footer-section2-contact.component';
import { FooterSection3QiuckLinksComponent } from "./footer-section3-qiuck-links/footer-section3-qiuck-links.component";

@Component({
  selector: 'app-footer',
  standalone: true,
  imports: [
    ContainerComponent,
    FooterSection1SubscribeComponent,
    FooterSection2ContactComponent,
    FooterSection3QiuckLinksComponent
],
  templateUrl: './footer.component.html',
  styleUrl: './footer.component.scss',
})
export class FooterComponent {}
