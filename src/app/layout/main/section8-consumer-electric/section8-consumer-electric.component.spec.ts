import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Section8ConsumerElectricComponent } from './section8-consumer-electric.component';

describe('Section8ConsumerElectricComponent', () => {
  let component: Section8ConsumerElectricComponent;
  let fixture: ComponentFixture<Section8ConsumerElectricComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Section8ConsumerElectricComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Section8ConsumerElectricComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
