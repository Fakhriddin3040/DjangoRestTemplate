import { TestBed } from '@angular/core/testing';

import { MoyskladService } from './moysklad.service';

describe('MoyskladService', () => {
  let service: MoyskladService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(MoyskladService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
