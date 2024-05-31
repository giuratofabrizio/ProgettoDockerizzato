import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AnimalsService {

  constructor(private http: HttpClient) { }
  
  //Il metodo fa una chiamata Http al server
  getAnimals() {
    return this.http.get<VettAnimal>("https://5000-giuratofabr-progettodoc-5bi8sj3suln.ws-eu114.gitpod.io/" + 'animals');
  }

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };
  sendNewAnimal(animal : Animal) : Observable<Animal>
  {
    return this.http.post<Animal>("https://5000-giuratofabr-progettodoc-5bi8sj3suln.ws-eu114.gitpod.io/" + 'newAnimal', animal,this.httpOptions)
  }
}

/*
Definisco il tipo di dato che mi aspetto di ricevere dal server 
"animals": [
  {
    "id": 1,
    "name": "Lion",
    "type": "wild"
  },
  ....
  }
]*/

export interface VettAnimal {
  [animals: string]: Animal[]
}
export interface Animal {
  id: string;
  name: string;
  type: any;
}
