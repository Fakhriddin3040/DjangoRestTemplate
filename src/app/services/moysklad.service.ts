  import { Injectable } from '@angular/core';
  import { HttpClient } from '@angular/common/http';
  import { Observable } from 'rxjs';
  import { BehaviorSubject } from 'rxjs';
  import { tap } from 'rxjs/operators';

  @Injectable({
    providedIn: 'root'
  })
  export class MoyskladService {

    private apiUrl = 'http://localhost:3000/proxy';
    private dataSubject = new BehaviorSubject<any[]>([]);

    data$ = this.dataSubject.asObservable();

    constructor(private http: HttpClient) { }    

    // Метод для получения данных с прокси сервера
    fetchData(): Observable<any> {
      return this.http.get<any>(this.apiUrl).pipe(
        tap(data => {
          console.log('Полученные данные:', data); // Лог данных в консоль браузера
          this.updateData(data); // Обновляем BehaviorSubject
        })
      );
    }

    // Метод для обновления данных в BehaviorSubject
    updateData(data: any[]) {
      console.log('MoyskladService - Сохранение данных в сервисе:', data); // Лог для проверки данных
      this.dataSubject.next(data);
    }
  }
