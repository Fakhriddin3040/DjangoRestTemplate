import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HeaderSection3UtilitiesComponent } from './header-section3-utilities.component';

describe('HeaderSection3UtilitiesComponent', () => {
  let component: HeaderSection3UtilitiesComponent;
  let fixture: ComponentFixture<HeaderSection3UtilitiesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [HeaderSection3UtilitiesComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(HeaderSection3UtilitiesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
