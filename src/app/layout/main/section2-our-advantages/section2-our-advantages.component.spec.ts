import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Section2OurAdvantagesComponent } from './section2-our-advantages.component';

describe('Section2OurAdvantagesComponent', () => {
  let component: Section2OurAdvantagesComponent;
  let fixture: ComponentFixture<Section2OurAdvantagesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Section2OurAdvantagesComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Section2OurAdvantagesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
