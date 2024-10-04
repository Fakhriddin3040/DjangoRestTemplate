import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProductSection4FilterComponent } from './product-section4-filter.component';

describe('ProductSection4FilterComponent', () => {
  let component: ProductSection4FilterComponent;
  let fixture: ComponentFixture<ProductSection4FilterComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ProductSection4FilterComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ProductSection4FilterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
