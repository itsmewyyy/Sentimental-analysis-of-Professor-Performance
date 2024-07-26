<template>
  <div :class="['textarea-container', containerSizeClass]">
    <label :for="id" class="textarea-label">{{ label }}</label>
    <textarea
      :id="id"
      :placeholder="placeholder"
      :rows="1"
      :cols="cols"
      :class="['textarea', textareaSizeClass, textareaColorClass]"
      :style="{ resize: 'none' }"
    ></textarea>
  </div>
</template>

<script>
export default {
  name: "TextAreaComponent",
  props: {
    id: {
      type: String,
      required: true,
    },
    label: {
      type: String,
      required: true,
    },
    placeholder: {
      type: String,
      default: "",
    },
    rows: {
      type: Number,
      default: 1,
    },
    cols: {
      type: Number,
      default: 40,
    },
    size: {
      type: String,
      validator: function (value) {
        return ["sm", "md", "lg"].includes(value);
      },
      default: "md",
    },
    color: {
      type: String,
      validator: function (value) {
        return ["white", "blue-50"].includes(value);
      },
      default: "white",
    },
  },
  computed: {
    containerSizeClass() {
      const sizeClasses = {
        sm: "container-sm",
        md: "container-md",
        lg: "container-lg",
      };
      return sizeClasses[this.size];
    },
    textareaSizeClass() {
      const sizeClasses = {
        sm: "textarea-sm",
        md: "textarea-md",
        lg: "textarea-lg",
      };
      return sizeClasses[this.size];
    },
    textareaColorClass() {
      const colorClasses = {
        white: "bg-transparent",
        "blue-50": "bg-transparent",
      };
      return colorClasses[this.color];
    },
  },
};
</script>

<style scoped>
.textarea-container {
  display: flex;
  flex-direction: column;
  margin-bottom: 1rem;
  border: 1px solid #ccc;
  border-top: 0;
  border-radius: 0.25rem;
  padding: 1rem;
  background: white;
}

.textarea-label {
  margin-bottom: 0.5rem;
  font-weight: 600;
}

.textarea {
  border: none;
  border-bottom: 1px solid #ccc;
  width: 100%;
  background: transparent;
  box-sizing: border-box;
}

.textarea:focus {
  outline: none;
  border-bottom: 1px solid black;
}

.container-sm {
  padding: 0.75rem;
}

.container-md {
  padding: 1rem;
}

.container-lg {
  padding: 1.5rem;
}

.textarea-sm {
  font-size: 0.875rem;
  padding: 0.5rem;
}

.textarea-md {
  font-size: 1rem;
  padding: 0.75rem;
}

.textarea-lg {
  font-size: 1.125rem;
  padding: 1rem;
}
</style>
