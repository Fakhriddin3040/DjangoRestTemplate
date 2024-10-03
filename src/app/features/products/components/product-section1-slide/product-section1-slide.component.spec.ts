import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProductSection1SlideComponent } from './product-section1-slide.component';

describe('ProductSection1SlideComponent', () => {
  let component: ProductSection1SlideComponent;
  let fixture: ComponentFixture<ProductSection1SlideComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ProductSection1SlideComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ProductSection1SlideComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
