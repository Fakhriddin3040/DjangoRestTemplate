import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Section10HealthyBeautyComponent } from './section10-healthy-beauty.component';

describe('Section10HealthyBeautyComponent', () => {
  let component: Section10HealthyBeautyComponent;
  let fixture: ComponentFixture<Section10HealthyBeautyComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Section10HealthyBeautyComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Section10HealthyBeautyComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
