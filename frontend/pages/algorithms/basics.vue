<template>
  <div class="sorting-container">
    <div class="header">
      <h1 class="title">Sorting Protocol</h1>
      <p class="subtitle">Visualizing data orchestration</p>
    </div>

    <div class="interface-panel card">
      <div class="input-section">
        <label for="data-input">Input Array:</label>
        <input 
          id="data-input"
          type="text" 
          v-model="inputString"
          placeholder="e.g., 5, 2, 8, 1, 9, 4" 
          class="data-input"
        />
        <button @click="runSort" :disabled="isLoading" class="btn">
          {{ isLoading ? 'Processing...' : 'Execute Sort' }}
        </button>
      </div>

      <div class="status-section">
        <div class="status-light" :class="statusClass"></div>
        <p>Status: {{ statusText }}</p>
      </div>

      <div v-if="sortedArray" class="output-section">
        <h3>Result Matrix:</h3>
        <code class="output-code">{{ sortedArray }}</code>
      </div>
      
      <div v-if="errorMsg" class="error-section">
        <h3>System Alert:</h3>
        <p>{{ errorMsg }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
// The script setup remains exactly the same. No changes needed.
import { ref, computed } from 'vue';

const inputString = ref('5, 2, 8, 1, 9, 4');
const sortedArray = ref(null);
const isLoading = ref(false);
const errorMsg = ref(null);

const statusText = computed(() => {
  if (isLoading.value) return 'Executing...';
  if (errorMsg.value) return 'Error';
  if (sortedArray.value) return 'Complete';
  return 'Idle';
});

const statusClass = computed(() => {
  if (isLoading.value) return 'status-processing';
  if (errorMsg.value) return 'status-error';
  if (sortedArray.value) return 'status-complete';
  return 'status-idle';
});

async function runSort() {
  isLoading.value = true;
  sortedArray.value = null;
  errorMsg.value = null;

  const numbers = inputString.value.split(',').map(num => Number(num.trim())).filter(num => !isNaN(num));
  
  if (numbers.length === 0) {
    errorMsg.value = "Invalid or empty array provided.";
    isLoading.value = false;
    return;
  }

  try {
    const { data, error } = await useFetch('http://127.0.0.1:8000/api/sort', {
      method: 'POST',
      body: { numbers }
    });

    if (error.value) {
      throw new Error(error.value.data?.message || 'Backend communication failure.');
    }

    sortedArray.value = data.value.sorted_numbers;
  } catch (err) {
    console.error('Failed to call sort API:', err);
    errorMsg.value = err.message;
  } finally {
    isLoading.value = false;
  }
}
</script>

<style scoped>
.sorting-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--spacing-large);
}

.header {
  text-align: center;
}

.interface-panel {
  width: 100%;
  max-width: 600px;
  display: flex;
  flex-direction: column;
  gap: var(--spacing-large);
}

.input-section {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-small);
}

.data-input {
  background-color: var(--background-color);
  color: var(--text-color);
  border: 1px solid var(--border-color);
  border-radius: var(--border-radius);
  padding: var(--spacing-medium);
  font-family: inherit;
  font-size: 1rem;
}

.status-section {
  display: flex;
  align-items: center;
  gap: var(--spacing-small);
  border: 1px solid var(--border-color);
  padding: var(--spacing-medium);
  border-radius: var(--border-radius);
}

.status-light {
  width: 15px;
  height: 15px;
  border-radius: 50%;
  transition: all 0.3s ease;
}
.status-idle { background-color: gray; }
.status-processing { background-color: orange; animation: pulse 1.5s infinite; }
.status-complete { background-color: var(--primary-color); }
.status-error { background-color: #ff0055; }

@keyframes pulse {
  0% { box-shadow: 0 0 0 0 rgba(255, 165, 0, 0.7); }
  70% { box-shadow: 0 0 0 10px rgba(255, 165, 0, 0); }
  100% { box-shadow: 0 0 0 0 rgba(255, 165, 0, 0); }
}

.output-section, .error-section {
  border-top: 1px solid var(--border-color);
  padding-top: var(--spacing-large);
}

.output-code {
  background-color: var(--background-color);
  padding: var(--spacing-medium);
  display: block;
  border-radius: var(--border-radius);
  white-space: pre-wrap;
  word-wrap: break-word;
}

.error-section {
  color: #ff0055;
}
</style>