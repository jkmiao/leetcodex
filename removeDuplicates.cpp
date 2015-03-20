// 给一个有序数列，删除重复的元素
//
class Solution{
		public:
				int removeDuplicates(int A[],int n){
						if(!n)
								return 0;
						int ret=1;
						for(int i=1;i<n;i++){
								if(A[i]!=A[i-1])
										A[ret++]=A[i];
						}
						return ret;
				}
};
