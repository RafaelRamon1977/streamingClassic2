import { Component, OnInit } from '@angular/core';
import {Movie, MoviesService} from '../movies.service';


@Component({
  selector: 'app-movie-list',
  templateUrl: './movie-list.component.html',
  styleUrls: ['./movie-list.component.scss']
})
export class MovieListComponent implements OnInit {

  movies: Array<Movie> | undefined;
  searchPattern: string = '';

  constructor(
    private moviesSrv: MoviesService,
  ) { }

  ngOnInit(): void {
    this.loadMovies();
  }

  loadMovies() {
    this.moviesSrv.list(this.searchPattern).subscribe((movies) => {
      this.movies = movies;
    });
  }

  clearSearch(): void {
    this.searchPattern = '';
  }

  onSearchChange(): void {
    this.loadMovies();
  }

}
