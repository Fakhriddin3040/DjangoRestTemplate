import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Section1ProductSlideComponent } from './section1-product-slide.component';

describe('Section1ProductSlideComponent', () => {
  let component: Section1ProductSlideComponent;
  let fixture: ComponentFixture<Section1ProductSlideComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Section1ProductSlideComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Section1ProductSlideComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
