<template>
  <div class="app-container">
    <header class="app-header">
      <nav class="navbar">
        <NuxtLink to="/" class="navbar-item">Home</NuxtLink>
        <NuxtLink to="/about" class="navbar-item">About</NuxtLink>
        <NuxtLink to="/contact" class="navbar-item">Contact</NuxtLink>
      </nav>
    </header>

    <main class="app-main">
      <slot />
    </main>
    
    <footer class="app-footer">
      <p>&copy; 2025 Algorithmic Playground</p>
    </footer>
  </div>
</template>

<style>
  /* Your existing styles are good. I've added a few for the navbar. */
  .app-container {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
  }
  .app-header {
    background-color: var(--surface-color);
    padding: var(--spacing-medium);
    border-bottom: 1px solid var(--border-color);
  }
  .navbar {
    display: flex;
    gap: var(--spacing-medium);
  }
  .navbar-item {
    text-decoration: none;
    color: var(--primary-color);
    font-weight: 500;
  }
  .app-main {
    background-color: var(--background-color);
    flex: 1;
    padding: var(--spacing-large);
  }
  .app-footer {
    background-color: var(--surface-color);
    padding: var(--spacing-medium);
    text-align: center;
    border-top: 1px solid var(--border-color);
    color: var(--primary-color);
  }
</style>