import { Component } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatMenuModule } from '@angular/material/menu';
import { MatIconModule } from '@angular/material/icon';
import { ContainerComponent } from '../../shared/container/container.component';
import {MatSelectModule} from '@angular/material/select';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatInputModule} from '@angular/material/input';


@Component({
  selector: 'app-header',
  standalone: true,
  imports: [
    MatButtonModule,
    MatMenuModule,
    MatIconModule,
    ContainerComponent,
    MatFormFieldModule, 
    MatSelectModule,
    MatInputModule
  ],
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss'],
  
})
export class HeaderComponent {
  imageUrl = 'assets/images/promo/promo1.png';
  imageUrl2 = 'assets/images/promo/promo2.png';
  selected = 'option2';
}
