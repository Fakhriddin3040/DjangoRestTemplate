import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Section9HomeGardenKitchenComponent } from './section9-home-garden-kitchen.component';

describe('Section9HomeGardenKitchenComponent', () => {
  let component: Section9HomeGardenKitchenComponent;
  let fixture: ComponentFixture<Section9HomeGardenKitchenComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Section9HomeGardenKitchenComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Section9HomeGardenKitchenComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
