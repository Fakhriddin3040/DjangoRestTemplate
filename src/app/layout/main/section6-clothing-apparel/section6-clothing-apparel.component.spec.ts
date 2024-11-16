import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Section6ClothingApparelComponent } from './section6-clothing-apparel.component';

describe('Section6ClothingApparelComponent', () => {
  let component: Section6ClothingApparelComponent;
  let fixture: ComponentFixture<Section6ClothingApparelComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Section6ClothingApparelComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Section6ClothingApparelComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
