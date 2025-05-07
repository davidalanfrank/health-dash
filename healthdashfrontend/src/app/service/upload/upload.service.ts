import { HttpClient, HttpHeaders, HttpParams, HttpRequest } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class UploadService {
  constructor(private http: HttpClient) {}

  getPresignedUrl(fileName: string, type: string) {
    let getheaders = new HttpHeaders().set('Accept', 'application/json');
    return this.http.post<any>('http://127.0.0.1:8000/presigned-url',{ file_name: fileName, type: type }, {headers: getheaders});
  }

  s3Upload(presignedUrl: any, formData: any) {
    const req = new HttpRequest('POST', presignedUrl, formData, {
      reportProgress: true,
      responseType: 'text',

    });


    console.log(req);
  
    return this.http.request(req);
  }

  extractData(fileName: string) {
    let getheaders = new HttpHeaders().set('Accept', 'application/json');
    return this.http.post<any>('http://127.0.0.1:8000/extract-data',{ file_name: fileName }, {headers: getheaders});
  }
  
}
