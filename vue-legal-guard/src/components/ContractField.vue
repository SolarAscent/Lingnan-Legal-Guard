<template>
  <div class="field" :class="{ 'field-wide': field.type === 'textarea' }">
    <label :for="field.key">{{ field.label }} <span v-if="field.required" aria-hidden="true">*</span></label>
    <select v-if="field.type === 'select'" :id="field.key" :value="modelValue" :disabled="disabled"
      :aria-required="field.required" :aria-invalid="Boolean(error)" :aria-describedby="error ? `${field.key}-error` : undefined"
      :class="{ invalid: error }" @change="$emit('update:modelValue', $event.target.value)">
      <option value="">请选择</option><option v-for="option in field.options" :key="option" :value="option">{{ option }}</option>
    </select>
    <textarea v-else-if="field.type === 'textarea'" :id="field.key" :value="modelValue" :disabled="disabled"
      :maxlength="field.maxLength" :placeholder="field.placeholder" :aria-required="field.required"
      :aria-invalid="Boolean(error)" :aria-describedby="error ? `${field.key}-error` : undefined"
      :class="{ invalid: error }" rows="3" @input="$emit('update:modelValue', $event.target.value)" />
    <input v-else :id="field.key" :value="modelValue" :disabled="disabled" :type="field.type === 'number' ? 'text' : field.type"
      :inputmode="field.type === 'number' ? 'decimal' : undefined" :maxlength="field.maxLength" :placeholder="field.placeholder"
      :aria-required="field.required" :aria-invalid="Boolean(error)" :aria-describedby="error ? `${field.key}-error` : undefined"
      :class="{ invalid: error }" @input="$emit('update:modelValue', $event.target.value)" />
    <p v-if="error" :id="`${field.key}-error`" class="field-error" role="alert">{{ error }}</p>
  </div>
</template>
<script setup>
defineProps({ field: Object, modelValue: String, error: String, disabled: Boolean })
defineEmits(['update:modelValue'])
</script>
<style scoped>
.field { display: grid; gap: 8px; min-width: 0; align-content: start; }
.field-wide { grid-column: 1 / -1; }
label { font-size: 14px; font-weight: 700; color: var(--ink); }
label span { color: #ab3829; }
input, textarea, select { width: 100%; min-width: 0; box-sizing: border-box; border: 1px solid #b9cec3; border-radius: 10px; padding: 12px; font: inherit; font-size: 15px; background: #fff; color: var(--ink); transition: border-color .18s, box-shadow .18s; }
textarea { resize: vertical; line-height: 1.6; }
input:focus, textarea:focus, select:focus { outline: 2px solid var(--green-700); outline-offset: 2px; border-color: var(--green-700); }
input:disabled, textarea:disabled, select:disabled { background: var(--cream); opacity: .7; }
.invalid { border-color: #ab3829; }
.field-error { color: #ab3829; font-size: 13px; margin: 0; }
@media (prefers-reduced-motion: reduce) { input, textarea, select { transition: none; } }
</style>
