import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from '../../services/api.service';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-login',
  templateUrl: 'login.page.html',
})
export class LoginPage {
  email = '';
  password = '';
  isRegister = false;
  error = '';

  constructor(
    private api: ApiService,
    private auth: AuthService,
    private router: Router
  ) {}

  submit(): void {
    this.error = '';
    const obs = this.isRegister
      ? this.api.register(this.email, this.password)
      : this.api.login(this.email, this.password);

    obs.subscribe({
      next: (res) => {
        this.auth.setToken(res.token);
        this.router.navigate(['/feed']);
      },
      error: (err) => {
        this.error = err.error?.message || 'An error occurred';
      },
    });
  }

  toggleMode(): void {
    this.isRegister = !this.isRegister;
    this.error = '';
  }
}
