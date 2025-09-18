<template>
  <div class="home-container">
    <div class="welcome-header">
      <h1 class="main-title">Algorithmic Playground</h1>
      <p class="subtitle">[ Do not leave without learning something new! ]</p>
    </div>
    
    <nav class="algorithm-grid">
      <NuxtLink to="/algorithms/basics" class="algo-card">Basics</NuxtLink>
      <NuxtLink to="/algorithms/sorting" class="algo-card">Sorting</NuxtLink>
      <NuxtLink to="/algorithms/searching" class="algo-card">Searching</NuxtLink>
      <NuxtLink to="/algorithms/graphs" class="algo-card">Graphs</NuxtLink>
      <NuxtLink to="/algorithms/dynamic-programming" class="algo-card">Dynamic Programming</NuxtLink>
      <NuxtLink to="/algorithms/data-structures" class="algo-card">Data Structures</NuxtLink>
    </nav>
  </div>
</template>

<style scoped>
.home-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--spacing-large);
}

.welcome-header {
  text-align: center;
}

.main-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: var(--primary-color-hover);
  margin-bottom: var(--spacing-small);
}

.subtitle {
  font-size: 1rem;
  color: var(--text-color);
  opacity: 0.8;
  margin: 0;
}

.algorithm-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--spacing-medium);
  width: 100%;
  max-width: 700px;
}

.algo-card {
  /* This creates the "frosted glass" look */
  background: rgba(26, 32, 53, 0.5); 
  backdrop-filter: blur(10px);
  border: 1px solid var(--border-color);
  color: var(--text-color);
  padding: var(--spacing-large) var(--spacing-medium);
  text-align: center;
  text-decoration: none;
  font-weight: 700;
  text-transform: uppercase;
  border-radius: var(--border-radius);
  transition: all 0.2s ease-in-out;
}

.algo-card:hover {
  /* Make the card lift and glow on hover */
  transform: translateY(-5px);
  color: var(--primary-color-hover);
  box-shadow: var(--glow-effect);
  background: rgba(26, 32, 53, 0.8);
}

/* Make the grid a single column on smaller screens */
@media (max-width: 600px) {
  .algorithm-grid {
    grid-template-columns: 1fr;
  }
}
</style>