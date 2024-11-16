import { Component, EventEmitter} from '@angular/core';
import { Section1BannerComponent } from "./header-section1-banner/header-section1-banner.component";
import { HeaderSection1OptionComponent } from "./header-section2-option/header-section2-option.component";
import { HeaderSection3UtilitiesComponent } from "./header-section3-utilities/header-section3-utilities.component";
import { HeaderSection4MenuComponent } from "./header-section4-menu/header-section4-menu.component"; 

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [    
    Section1BannerComponent,
    HeaderSection1OptionComponent,
    HeaderSection3UtilitiesComponent,
    HeaderSection4MenuComponent
],
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss'],
})
export class HeaderComponent{
  
  
}