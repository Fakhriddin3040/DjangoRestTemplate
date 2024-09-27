import { Component, EventEmitter, Output, ViewChild, AfterViewInit, OnInit } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatMenuModule } from '@angular/material/menu';
import { MatIconModule } from '@angular/material/icon';
import { ContainerComponent } from '../../shared/container/container.component';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';

import { Section1BannerComponent } from "./header-section1-banner/header-section1-banner.component";
import { HeaderSection1OptionComponent } from "./header-section2-option/header-section2-option.component";
import { HeaderSection3UtilitiesComponent } from "./header-section3-utilities/header-section3-utilities.component"; 

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [
   
    MatMenuModule,
    MatIconModule,
    ContainerComponent,
    MatFormFieldModule,
    MatInputModule,
  

    Section1BannerComponent,
    HeaderSection1OptionComponent,
    HeaderSection3UtilitiesComponent
],
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss'],
})
export class HeaderComponent{
  
  
}