import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from '../../services/api.service';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-feed',
  templateUrl: 'feed.page.html',
})
export class FeedPage implements OnInit {
  items: any[] = [];
  newCaption = '';
  newUrl = '';

  constructor(
    private api: ApiService,
    private auth: AuthService,
    private router: Router
  ) {}

  ngOnInit(): void {
    if (!this.auth.isLoggedIn()) {
      this.router.navigate(['/login']);
      return;
    }
    this.loadFeed();
  }

  loadFeed(): void {
    const token = this.auth.getToken();
    if (!token) return;
    this.api.getFeed(token).subscribe({
      next: (res) => (this.items = res.rows || []),
      error: () => this.router.navigate(['/login']),
    });
  }

  addPost(): void {
    const token = this.auth.getToken();
    if (!token || !this.newCaption || !this.newUrl) return;
    this.api.createFeedItem(token, this.newCaption, this.newUrl).subscribe({
      next: () => {
        this.newCaption = '';
        this.newUrl = '';
        this.loadFeed();
      },
    });
  }

  logout(): void {
    this.auth.logout();
    this.router.navigate(['/login']);
  }
}
