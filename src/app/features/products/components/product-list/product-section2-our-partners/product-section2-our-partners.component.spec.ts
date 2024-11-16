import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProductSection2OurPartnersComponent } from './product-section2-our-partners.component';

describe('ProductSection2OurPartnersComponent', () => {
  let component: ProductSection2OurPartnersComponent;
  let fixture: ComponentFixture<ProductSection2OurPartnersComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ProductSection2OurPartnersComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ProductSection2OurPartnersComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
