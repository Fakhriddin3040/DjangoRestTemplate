import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProductSection3CategoryElectronicsComponent } from './product-section3-category-electronics.component';

describe('ProductSection3CategoryElectronicsComponent', () => {
  let component: ProductSection3CategoryElectronicsComponent;
  let fixture: ComponentFixture<ProductSection3CategoryElectronicsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ProductSection3CategoryElectronicsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ProductSection3CategoryElectronicsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
