import {Component, OnInit, ViewChild} from '@angular/core';
import LocationsJSON from "../assets/locations.json";
import CitesJSON from "../assets/cities.json";
import {MatSidenav} from "@angular/material/sidenav";

interface LOCATION {
  lat: number,
  lng: number
}

interface CITIES {
  name: string,
  lat: number,
  lng: number
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'container';
  locations: LOCATION[] = LocationsJSON
  cities: CITIES[] = CitesJSON
  default_lat = 51.678418;
  default_lng = 7.809007;
  default_zoom = 6;

  handleClick($event: MouseEvent, city: CITIES) {
    console.log(city.name)
    this.default_lat = city.lat
    this.default_lng = city.lng
    this.default_zoom = 12
  }

  @ViewChild('sidenav') sidenav: MatSidenav;
  isExpanded = false;
  showCitySubmenu: boolean = false;
  showSettingSubmenu: boolean = false;
  isShowing = false;

  mouseenter() {
    if (!this.isExpanded) {
      this.isShowing = true;
    }
  }

  mouseleave() {
    if (!this.isExpanded) {
      this.isShowing = false;
    }
  }

}
