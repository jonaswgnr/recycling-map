import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AgmCoreModule } from '@agm/core';
import { AgmMarkerClustererModule, ClusterManager } from '@agm/markerclusterer';

import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {MatToolbarModule} from "@angular/material/toolbar";
import {MatIconModule} from "@angular/material/icon";
import {MatButtonModule} from "@angular/material/button";
import {MatMenuModule} from "@angular/material/menu";

@NgModule({
  declarations: [
    AppComponent
  ],
    imports: [
        BrowserModule,
        AgmCoreModule.forRoot({
            apiKey: ''
        }),
        AgmMarkerClustererModule,
        BrowserAnimationsModule,
        MatToolbarModule,
        MatIconModule,
        MatButtonModule,
        MatMenuModule
    ],
  providers: [ClusterManager],
  bootstrap: [AppComponent]
})
export class AppModule { }


