import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class MoyskladService {

  private apiUrl = 'http://localhost:3000/proxy';
  constructor(private http: HttpClient) { }

  // Метод для получения данных с прокси сервера
  fetchData(): Observable<any> {
    return this.http.get<any>(this.apiUrl);
  }
}
