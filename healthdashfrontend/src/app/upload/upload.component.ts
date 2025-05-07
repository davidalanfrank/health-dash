import { Component } from '@angular/core';
import { UploadService } from '../service/upload/upload.service';

@Component({
  selector: 'app-upload',
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.css'],
})
export class UploadComponent {
  private fileName: string = '';
  constructor(private uploadService: UploadService) {}

  onFileUpload(fileInput: any, type: any) {


    this.uploadService.getPresignedUrl(fileInput.files[0].name, type).subscribe(res => {

      if (res.success) {
        const formData: FormData = new FormData();
        Object.keys(res.data.fields).forEach(key => formData.append(key, res.data.fields[key]));
        this.fileName = fileInput.files[0].name;
        formData.append('file', fileInput.files[0], fileInput.files[0].name);
        this.uploadService.s3Upload(res.data.url, formData).subscribe(res => {
          console.log(" UPLOAD  res",res);

          if((res as any).status == 204){


            this.uploadService.extractData(this.fileName).subscribe((res: any) => {


            })
          }
        });
      }
    });
  }
}