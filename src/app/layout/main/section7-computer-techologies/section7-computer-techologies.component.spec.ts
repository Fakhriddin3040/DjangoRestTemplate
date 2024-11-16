import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Section7ComputerTechologiesComponent } from './section7-computer-techologies.component';

describe('Section6ClothingApparelComponent', () => {
  let component: Section7ComputerTechologiesComponent;
  let fixture: ComponentFixture<Section7ComputerTechologiesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Section7ComputerTechologiesComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Section7ComputerTechologiesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
