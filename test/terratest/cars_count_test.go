package test

import (
	"os/exec"
	"strings"
	"testing"

	"github.com/gruntwork-io/terratest/modules/logger"
	"github.com/gruntwork-io/terratest/modules/terraform"
	"github.com/stretchr/testify/assert"
)

func TestTerraformExternalData(t *testing.T) {
	pythonVersion, error := exec.Command("python", "--version").Output()
	if error != nil {
		logger.Log(t, error)
	}
	logger.Log(t, strings.TrimSuffix(string(pythonVersion), "\n"))

	t.Parallel()
	terraformOptions := &terraform.Options{
		TerraformDir: "../../examples",
		NoColor:      true,
	}
	defer terraform.Destroy(t, terraformOptions)
	terraform.InitAndApply(t, terraformOptions)

	cars_count := terraform.Output(t, terraformOptions, "cars_count")

	var stringTest string
	assert.IsType(t, stringTest, cars_count)

	var counts [5]string = [5]string{"0", "1", "2", "3", "4"}
	assert.Contains(t, counts, cars_count)
}
