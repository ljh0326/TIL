#Data Structures & Algorithms 번역하기 프로젝트

## Cording Interview Algorithms

### Arrays
#### 1.Two Sum()
#####문제
Given an array of integers, return indices of the two numbers such that they add up to specific target
정수 배열이 주어졌을 때, 더했을 경우 특정 수를 만족하는 두 숫자의 인덱스를 반환하시오

you may assume that each input would have exactly one solution, and you may not use the same element twice.
각 입력당 정확한 하나의 풀이방법이 있다고 가정하십시요 그리고 요소를 중복해서 사용할 수 없습니다.
  
Example:
Given nums = [2, 7, 11, 15], target = 9,

Becuase num[0] + num[1] = 2 + 7 = 9,
return [0, 1].

#####Program Structure;
<pre><code>
public class Solution{
	public int[] twoSum(int[] nums, int target){
    
    }
}
</code></pre>

##### 해결법
We can solve this problem with O(N) time complexity using a HashMap.
우리는 이 문제를 해쉬맵을 사용해서 O(N)의 시간복잡도로 풀 수 있습니다. 
<pre><code>
public int[] twoSum(int[] nums, int target) {
		
		//결과를 바놯하는 배열
        int[] arr = new int[2];
        
        //num및 index 쌍에 대한 맵.
        Map<Integer, Integer>map = 
        		new HashMap<Integer, Integer>();
        
        //배열 순환
        for(int i = 0; i < nums.length; i++) {
        	
        	//맵에 타겟과 현제 요소의 차이와 같은 요소가 있는지 체크
        	Integer val = map.get(target - nums[i]);
        	if(val == null) {
        		//값이 없다면, 현재 요소와 인덱스를 맵에 추가
        		map.put(nums[i], i);
        	} else {
        		
        		//값이 있다면 인덱스 값을 업데이트 
        		arr[0] = val;
        		arr[1] = i;
        		break; // 반복문 탈출
        	}
        	
        }
		return arr;
	}
</code></pre>

#### 시간복잡도 : O(N)
The array is traversed only once. So the tie complexity is directly proportional to the size of the array
배열은 한번만 통과됩니다. 그래서 시간복잡도는 배열의 크기에 비례합니다.

#### 공간복잡도 : O(N)
O(1) + O(N) = O(N) O(1)for the variables and O(N) for the hashmap. For hashmap, with the increase of the number of entries, the hashmap's space will increase linearly. So space complexity of hashmap is O(N)
O(1)은 변수 때문이며, O(N)은 해쉬맵 때문입니다. 엔트리가 증가할 수록 해쉬맵의 공간은 선형적으로 늘어날 것입니다. 그래서 해쉬맵의 공간복잡도는 O(N)입니다.

난이도 : 쉬움
### 알게된 영단어
indices : 지수, 색인
add up to : 합계하다.
aussme : 가정하다.
difference : 차
traverse : 횡단, 선회
proportional : 비례항
proportion : 비례, 비율
entries : 항목

_ _ _

#### 2. Container With Most Water
##### 문제
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate(i,ai).
각각 좌표(i,ai)에 있는 점을 나타내는 음수가 아닌 정수 a1, a2, ..., an이 주어졌을 때

n vertical lines are drawn such that the two endpoints of line i is at(i, ai) and (i,0).
선의 양 끝점인(i,ai) 와 (i,0) 을 기준으로 n개의 수직선이 그려진다. 

Find two lines, which toerher with x-axis forms a container, such that the container contains the most water.
가장 많은 물을 포함한 컨테이너를 만드는 두 선을 찾으세요.

Note: You may not slant the container and n is al least 2.
주의 : 컨테이너를 기울이지 말고, n은 적어도 2입니다.

##### Soution
<pre><code>
public int maxArea(int[] height) {
		
	}
</code></pre>

##### Solution
AKA, the general idea to find some max is to go through all cases where max value can possibly occur and keep updating the max value.
보통, 어떤 최대값을 찾는 방법은 최대값이 나올 수 있는 모든 경우를 살펴보고 최대값을 계속 업데이트 하는 것 입니다.
The efficiency of the scan depends on the size of cases you plan to scan.
탐색의 효율성은 당신의 탐색 계획 크기에 따라 다릅니다.

To increase efficiency, all we need to do is to find a smart way of scan to cut off the useless cases and meanwhile 100% guarantee the max value can be reached through the rest of cases.
효율을 높이기 위해, 우리는 쓸모없는 케이스를 줄이고 나머지 케이스를 통해 최대값에 100% 도착하는 스마트한 스캔 방법을 찾아야 합니다.

in this problem, the smart scan way is to set two pointers initialized at both ends of the array.
이 문제에서, 스마트한 스캔 방법은  배열의 양쪽 끝에 초기화 된 두 개의 포인터를 설정하는 것입니다.

Every time move the smaller value pointer to inner array. Then after the two pointers meet, all possible max cases have been scanned and the max situation is 100 reached somewhere in the scan. 
매번 작은값의 포인터를 내부배열로 이동하세요 그 다음 두개의 포인터가 만나면, 모든 케이스가 검색되고 검색 어딘가에 최댓값이 100% 있습니다.

Follwing is a brief prove of this.
뒤에 요약된 증명이 나옵니다.

Given a1, a2, a3 ... an as input array. Lets assume a10 and a20 are the max area situation. We need to prove that a10 can be reached by left pointer and during the time left pointer stays at a10, a20 can be reached by right pointer. during the time
a1, a2 ,a3 ... 값이 배열에 담겨서 주어졌을 때. a10과 a20이 가장 큰 넓이를 갖는다고 가정하자. 우리는 왼쪽 포인터로 a10에 도착할 수 있는것을 증명해야 하고 왼쪽 포인터가 a10에 머무는 동안 오른쪽 포인트는 a20에 도착 할 수 있다.

That is to say, the core problem is to prove: when left pointer is at a10 and right pointer is at a21, the next move must be right pointer to a20.
즉,증명의 핵심은 왼쪽 포인터가 a10에 있고 오른쪽 포인터가 a21에 있을 때, 다음 움직임에서 오른쪽 포인터는 a20이 되야한다는 것이다.

Since we are always moving the pointer with the smaller value, if a10 > a20, we should move pointer at a21 to a20, as we hope. Why a10>a21? Because if a21>a10, then area of a10 and a20 must be less than area of a10 and a21. Because the area of a10 and a21 is at least height[a10]*(21-10) while the area of a10 and a20 is at most height[a10]*(20-10). So there is a contradiction of assumption a10 and a20 has the max area. So, a10 must be greater than a21, then next move a21 has to be move to a20. The max cases must be reached.
우리는 항상 포인터를 더 작은 값으로 움직이기 때문에, 만약 a10이 a20보다 크다면 우리는 a21을 a20으로 옮겨야 한다.
왜 그래야하냐면, 만약 a21>a10이라면 a10에서 a20까지의 넓이가 a10에서a21의 넓이보다 더 작기 때문이다. 왜냐하면
a10에서 a21까지의 넓이는 height[a10] *(21-10)이고 a10에서a20까지의 넓이는 height[a10] * (20-10)이기 때문이다. 그래서 a10부터 a20이 최대넓이라는 것은 모순된다. 따라서 a10은 a21보다 커야하며 그렇기 때문에 a21을 a20으로 옮겨야 한다. 최대크기에 반드시 도착해야 한다.

<pre><code>
public int maxArea(int[] height) {
		int left = 0, right = height.length - 1;
		int maxArea = 0;
		
        //모든 배열을 다 돌면서
		while(left < right) {
        	//맥스값 구하기
			maxArea = Math.max(maxArea,  Math.min(height[left], height[right])
					* (right - left));

			//더 작은값이 있다면 큰값으로 옮기기
			if(height[left] < height[right])
				left++;
			else
				right--;
		}
		return maxArea;
	}
</code></pre>

##### 시간 복잡도 : O(N)
This solution runs in O(N) time complexity where N is the size of the array.
이 해결법은 O(N)의 시간복잡도를 가집니다. N은 배열의 크기입니다.

##### 공간 복잡도 : O(1)
This algorithm uses a constant extra space.
이 알고리즘은 일정한 공간을 사용합니다.

### 알게된 영단어
coordinate 동등 어구
represent : 말하다. 표현하다 묘사하다.
slant : 경사
AKA : 일명
go through : 통과하다, 완료하다
meanwhile : 그 동안에, 한편
during the time : 그 시간동안
is at~ : ~에 있다.
constant : 일정한, 상수
i.e : 즉
at least : 적어도
contradiction : 모순

* * *
### Strings
#### 1.Longest Substring Without Repeating Characters
#####문제
Given a string, find the length of the longest substring without repeating characers.
문자열이 주어졌을 때, 중복된 문자를 제외한 가장 긴 문자열을 찾아라
<pre>
Example:
Given "abcabcbb", the answer is "abc" which the length is 3
Given "bbbbb", the answer is "b" with the length of 1.
</pre>

<pre>
Program Structure;
public int lengthOfLongestSubstring(String s){

}
</pre>

##### Solution
The basic idea is, keep a hashmap which stores the characters in string as keys and their positions as values, and keep two pointers which define the max substring
기본적으로, 문자열의 문자를 키값으로 하고 문자의 인덱스값을 값으로 가진 해쉬맵과 가장 큰 하위문자열을 정의하는 포인터 2개를 유지하세요.

Move the right pointer to scan through the string, and meanwhile update the hashmap.
오른쪽 포인터를 이동하여 문자열을 스캔하고 해시 맵을 업데이트합니다.

if the character is already in the hashmap, then move the left pointer to the right of the same character last found.
만약 문자가 이미 해쉬맵에 있다면, 마지막으로 찾은 동일한 문자의 오른쪽으로 왼쪽 포인터를 이동하십시오.

Note that the two pointers can only move forward.
두개의 포인터는 앞으로만 움직인다는 것을 기억하세요
<pre>
<code>
//만약 긴문자열도 출력하라고하면 배열을 이용해보자
public int lengthOfLongestSubstring(String s) {
		if(s.length() == 0)
			return 0;
		
		int max = 0;
		
		HashMap<Character, Integer> map = new HashMap<Character, Integer>();
		for(int i = 0; i < s.length(); i ++) {
			if(map.containsKey(s.charAt(i))){
				continue;
			}
			
			map.put(s.charAt(i), i);
		}
		
		return map.size();
	}
</code>
</pre>

##### 시간복잡도 : O(N)
The soulution runs in O(N) time complexity where N is the size of the Stirng.
해법의 시간복잡도는 O(N)이며 N은 문자열의 길이이다.

##### 공간복잡도 : O(N)
This algorithm uses an extra space of size N.
이 알고리즘은 크기 N의 추가 공간을 사용합니다.


###알게된 영단어
substring : 하위문자열

#### 2.Longest Palindromic Substring
##### 문제
Given a stirng s, find th longest palindromic substinrg in s. You may assume that the maximum length of s is 1000.
문자열 s가 주어졌을 때, 문자열 안에서 가장 긴 회문을 구하여라. 단 문자열의 최대 크기는 1000이라고 가정한다.
<pre>
Example:

Input: "babad"
Output: "bab" 

Note "aba" is also a valid answer.
Example:

Input: "cbbd"
Output: "bb"
</pre>

Program Structure:
<pre>
public String longestPalindrome(String s){

}
</pre>

##### Solution
Each character is considered as the mid of a palindrome string and the largest palindrome is checked.
각 문자는 회문의 중심문자로 고려되며 가장 긴 회문이 답이된다.
<pre><code>

private int lo, maxLen;

public String longestPalindrome(String s) {
		int len = s.length();
		if (len < 2) return s;
		
		for (int i = 0 ;i < len - 1; i++) {
			//홀수길이일 때
			extendPalindrome(s, i, i);
			//짝수길이일 때
			extendPalindrome(s, i, i+1);
		}
		
		return s.substring(lo,  lo + maxLen);
	}
	
	private void extendPalindrome(String s, int j, int k) {
		while( j >= 0 && k < s.length() && s.charAt(j)==s.charAt(k)) {
			j--;
			k++;
		}
		
		if(maxLen < k - j -1) {
			lo = j + 1;
			maxLen = k - j - 1;
		}
	}
</code></pre>

##### 시간복잡도 : O(N^2)
Consider N as the length of the string, the extendPalindrome() method is called 2N times. The complexity of extendPalindrome() itself is O(N) which makes the total time complexity as O(2N^2) = O(N^2)
문자열의 길이를 N이라고 가정하면 extendPalindrome() 메서드는 2N 번 호출됩니다. extendPalindrome()자체의 복잡성은 O (N)이며, 이는 O(2N^2) = O (N^2)

##### 공간복잡도 : O(1)
This algorithm uses a constant extra space.
이 알고리즘은 일정한 추가 공간을 사용합니다.

### 알게된 영단어
Palindromic : 회문


* * *

### Two Pointers
#### 1. Longest Common Prefix
##### 문제
Write a function to find the longest common prefix string amongst an array of string
문자열의 배열 중에서 가장 긴 공통 접두사 문자열을 찾는 함수를 작성하십시오.

<pre>
Program Structure;
public String longestCommonPrefix(String[] strs){

}
</pre>

##### Solution
Sort the array first, and then you can simply compare the fist and last elements in the sorted array.
먼저 배열을 정렬하면 간단하게 정렬된 배열의 첫번째 요소와 마지막요소를 비교할 수 있습니다.

<pre>
<code>
public String longestCommonPrefix(String[] strs) {
		StringBuilder result = new StringBuilder();
		
		if(strs != null && strs.length > 0) {
			Arrays.sort(strs);
			
			char[] a = strs[0].toCharArray();
			char[] b = strs[strs.length-1].toCharArray();
			
			for(int i = 0 ; i < a.length; i++) {
				if(b.length > 1 && b[i] == a[i]) {
					result.append(b[i]);
				}else {
					return result.toString();
				}
			}	
		}
		return result.toString();
	}
</code>
</pre>

### 알게된 영단어
amongst : 사이에

- - -

#### 2. 3Sum
##### 문제
Given an array S of n integers, are there elements a, b, c, in S such that a + b+ c = 0? Find all unique triplets in the array which gives the sum of zero.
n개의 정수로 이루어진 배열 S가 주어졌을 때, S에 있는 요소 중 a, b, c = 0 인 요소가 있는가? 배열에서 합계가 0인 고유 삼중항을 찾아라.

Note : The solution set must not contain duplicate triplets.
주의 : 솔루션 세트는 중복 된 쌍을 포함하지 않아야합니다.
##### For example, given array S = [-1, 0, 1, 2, -1, -4],
<pre>
A solution set is:
[
	[-1, 0, 1],
    [-1, -1, 2]
]
</pre>

##### Program Structure
<pre>
public class Solution{
	public List<List<Integer>> threeSum(int[] nums){
    
    }
}
</pre>


##### Solution
The idea is to sort an input array and then run through all indices of a possible first element of a triplet.
방법은 배열을 정렬한 후 삼중항의 첫번째 요소가 될 수 있는 모든 지수를 조사하는 것 입니다.
For each possible first element we make a standard bi-directional 2Sum sweep of the remaining part of the array. 
각각의 첫번째 요소에 대해 우리는 배열의 나머지 부분에 대해 표준 양방향 2Sum 스윕을 만듭니다.
Also we want to skip equal elements to avoid duplicates in the answer.
또한 중복된 답을 피하기위해 같은 요소들은 스킵해야 합니다.

<pre>
<code>

</code>
</pre>

##### 시간복잡도 : O(N^2)
All elements in the list are processed for every index.
### 알게된 영단어
triplets : 세쌍둥이
indices : 지수
bi-directional : 양방향
