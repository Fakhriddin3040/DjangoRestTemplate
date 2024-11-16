import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProductSettingFilterComponent } from './product-setting-filter.component';

describe('ProductSettingFilterComponent', () => {
  let component: ProductSettingFilterComponent;
  let fixture: ComponentFixture<ProductSettingFilterComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ProductSettingFilterComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ProductSettingFilterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
